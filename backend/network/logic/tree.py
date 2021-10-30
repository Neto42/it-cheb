import logging

from django.utils import timezone
from joblib import dump
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from network.logic.variable import path_tree
from network.models import Network
from network.serializers import NetworkSerializer

logger = logging.getLogger(__name__)


def get_data(size=None):
    if size:
        network = Network.objects.all()[0:size]
        serializer = NetworkSerializer(network, many=True)
    else:
        network = Network.objects.all()
        serializer = NetworkSerializer(network, many=True)

    network = []
    for i in serializer.data:
        network.append(dict(i))

    df = pd.DataFrame(network)
    df = df.drop(columns='street')
    df = df.drop(columns='object_type')
    print(df)

    return df


def df_education(size=None):
    education = get_data(size)
    y = np.array(education['construction'])
    x = education.drop('construction', axis=1)
    x_list = list(x.columns)
    x = np.array(x, dtype=np.int64)
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)

    return train_x, test_x, train_y, test_y, x_list, education


def tree(size=None, n_jobs=1, name=path_tree):
    start = timezone.now()

    train_x, test_x, train_y, test_y, x_list, education = df_education(size)
    classifier = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=n_jobs)
    classifier.fit(train_x, train_y)

    rez = classifier.predict(test_x)

    tree_save(classifier, name)

    print(f'Обучение заняло:{(timezone.now() - start).seconds}с')
    print(f'Rez:{rez}с')

    return classifier


def tree_save(regressor, name=path_tree):
    dump(regressor, name)
