from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskCreateSerializer
from .models import AWSCredentials
from rest_framework.permissions import IsAuthenticated


class AWSTaskAPIView(APIView):
    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data.copy()
        data['user_id'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            AWSCredentials.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data)
        return Response(serializer.errors, 400)


class GetAWSInstanceStateAPIView(APIView):
    def get_filter(self):
        _filter = {"state": self.request.query_params.get('state')}
        return _filter

    def get(self):
        pass


class GetAllUserAWSDataAPIView(APIView):
    def get(self):
        pass







