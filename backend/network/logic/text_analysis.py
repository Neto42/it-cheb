import logging
import random

import pandas as pd
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem.snowball import SnowballStemmer

from city.models import City
from network.models import Network
from network.serializers import NetworkSerializer
from statement.models import Statement
from statement.serializers import StatementSerializer

logger = logging.getLogger(__name__)

MIN_SIZE = 0
MAX_SIZE = 5000


def text():
    object_type_list = [
        'спортивн',
        # 'игровая',
        'тротуар',
        # 'освещение',
        # 'парк',
        # 'сквер',
        # 'аллея',
        # 'дорога',
        # 'ТБО',
    ]

    statement = Statement.objects.all()
    serializer = StatementSerializer(statement, many=True)

    statement = []
    for i in serializer.data:
        statement.append(dict(i))

    df = pd.DataFrame(statement)

    tk = WhitespaceTokenizer()

    for i in range(len(df)):
        object_type = tk.tokenize(str(df['complaint'][i]).lower())
        social_type = df['social'][i]
        street_id = df['city'][i]
        street = City.objects.get(pk=street_id).street
        size = random.randint(MIN_SIZE, MAX_SIZE)

        if social_type == 1 or social_type == 2 or social_type == 5:
            social_n = True
        else:
            social_n = False

        if size > 1000:
            construction = True
        else:
            construction = False

        for obj in object_type:
            if SnowballStemmer('russian').stem(obj) in object_type_list:
                data = {
                    'passability': size,
                    'object_type': obj,
                    'social': social_n,
                    'street': street,
                    'construction': construction,
                }
                serializer = NetworkSerializer(data=data)

                if serializer.is_valid():
                    serializer.validated_data
                    serializer.save()
                else:
                    print(serializer.errors)
