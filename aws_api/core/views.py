# from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskCreateSerializer


class AWSTaskAPIView(APIView):
    serializer_class = TaskCreateSerializer

    def post(self, request):
        data = request.data.copy()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            # print(serializer.data)
            print(serializer.validated_data)
            return Response("andar se")
        #     return Response(serializer.data, 200)
        # return Response(serializer.errors, 400)
        return Response(serializer.errors)
