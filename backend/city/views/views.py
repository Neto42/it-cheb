from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from city.models import City, PopulationSize, SocialStatuses
from city.serializers import CitySerializer, PopulationSerializer, SocialStatusesSerializer


class CityList(APIView):
    def get(self, request):
        profile = City.objects.all()
        serializer = CitySerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PopulationList(APIView):
    def get(self, request):
        profile = PopulationSize.objects.all()
        serializer = PopulationSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PopulationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SocialStatusesList(APIView):
    def get(self, request):
        profile = SocialStatuses.objects.all()
        serializer = SocialStatusesSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SocialStatusesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
