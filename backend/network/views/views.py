from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from network.models import Network
from network.serializers import NetworkSerializer


class NetworkList(APIView):
    def get(self, request):
        profile = Network.objects.all()
        serializer = NetworkSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NetworkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

