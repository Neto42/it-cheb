from rest_framework import serializers

from network.models import Network, Rezult


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'


class RezultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezult
        fields = '__all__'

