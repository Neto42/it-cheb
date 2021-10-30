from rest_framework import serializers

from city.models import City, PopulationSize, SocialStatuses


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationSize
        fields = '__all__'


class SocialStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialStatuses
        fields = '__all__'
