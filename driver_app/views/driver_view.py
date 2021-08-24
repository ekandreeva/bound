from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.decorators import action

from bound_api.serializers import UserSerializer, OrderSerializer
from driver_app.serializers import DriverSerializer, VehicleSerializer


class DriverViewSet(viewsets.ModelViewSet):

    permission_classes = [AllowAny]

    @action(detail=False, methods=['put'])
    def update_profile(self, request):
        user = request.user
        data = request.data
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.update(user, data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def add_vechicle(self, request):
        data = request.data
        driver = request.user.driver.pk
        data['driver'] = driver
        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def orders(self, request):
        driver = request.user.driver
        orders = driver.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response( serializer.data, status=status.HTTP_200_OK )

    # @action(detail=False, methods=['put'])
    # def accept_order(self, request, order_id):
    #     driver = request.user.driver
    #     driver.
    #     serializer = OrderSerializer(orders, many=True)
    #     return Response( serializer.data, status=status.HTTP_200_OK )
