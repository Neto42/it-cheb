import logging

from django.core.paginator import Paginator
from django.utils import timezone
from joblib import load
import pandas as pd

from network.logic.variable import path_tree
from network.models import Network, Rezult
from network.serializers import NetworkSerializer, RezultSerializer

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
    df = df.drop(columns='construction')
    print(df)

    return df


def prediction(size=None, n_jobs=1, name=path_tree):
    start = timezone.now()

    clf = load(name)
    df = get_data(size)
    clf.n_jobs = n_jobs
    rezult = clf.predict(df)

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
    df = df.drop(columns='construction')
    df['rezult'] = rezult
    print(df)
    data = df.to_dict('records')

    Rezult.objects.all().delete()
    pr = RezultSerializer(data=data, many=True)

    pr.is_valid(raise_exception=True)

    paginator = Paginator(pr.data, 500)
    logger.info(f'Создание предсказаний: {paginator.count}')

    for page in range(paginator.num_pages):
        predictions = [Rezult(**item) for item in paginator.get_page(page)]
        Rezult.objects.bulk_create(predictions)

    logger.info(
        f'Предсказано продлений: {Rezult.objects.all().count()}. '
        f'Заняло:{(timezone.now() - start).seconds}с'
    )
