from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from statement.models import Statement
from statement.serializers import StatementSerializer


class StatementList(APIView):
    def get(self, request):
        profile = Statement.objects.all()
        serializer = StatementSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StatementSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
