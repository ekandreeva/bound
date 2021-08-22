from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.decorators import action

from bound_api.serializers import UserSerializer
from driver_app.serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):

    permission_classes = [AllowAny]

    # @action(detail=False, methods=['put'])
    # def update_profile(self, request):
    #     user = request.user
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # @action(detail=False, methods=['put'])
    # def add_vechicle(self, request):
    #     driver = request.user.driver
    #     vehicle = Vehicle.
    #     serializer = DriverSerializer(driver)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
