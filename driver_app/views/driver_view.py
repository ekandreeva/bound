from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from datetime import datetime
from bound.permission import DriverOnly
from bound_api.serializers import UserSerializer, OrderSerializer, PhotoSerializer
from bound_api.models import Photo
from driver_app.serializers import DriverSerializer, VehicleSerializer
from driver_app.models import Driver


class DriverViewSet(viewsets.ModelViewSet):
    permission_classes = [DriverOnly]

    @action(detail=False, methods=['patch'])
    def update_profile(self, request):
        user = request.user
        data = request.data
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.update(user, data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def add_photo(self, request):
        driver = request.user.driver
        photo = Photo(url=request.data['url'], type=request.data['type'], content_object=Driver.objects.last())
        serializer = DriverSerializer(driver)
        return Response( serializer.data, status=status.HTTP_200_OK )

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

    @action(detail=False, methods=['put'])
    def accept_order(self, request, order_id):
        driver = request.user.driver

        order_driver = driver.orders_drivers.get(order=order_id)
        order_driver.accepted=True
        order_driver.save()

        order = order_driver.order
        order.accepted_at = datetime.now()
        order.status = 'Accepted'
        order.save()

        content = {
            "success": True
        }
        return Response( content, status=status.HTTP_200_OK )

    @action(detail=False, methods=['put'])
    def drop_order(self, request, order_id):
        driver = request.user.driver

        order_driver = driver.orders_drivers.get(order=order_id)
        order_driver.accepted=False
        order_driver.save()

        order = order_driver.order
        order.droped_at = datetime.now()
        order.status = 'Dropped'
        order.save()

        content = {
            "success": True
        }
        return Response( content, status=status.HTTP_200_OK )

    @action(detail=False, methods=['put'])
    def pick_order(self, request, order_id):
        driver = request.user.driver

        order_driver = driver.orders_drivers.get(order=order_id)
        order_driver.accepted=False
        order_driver.save()

        order = order_driver.order
        order.picked_at = datetime.now()
        order.status = 'Picked'
        order.save()

        content = {
            "success": True
        }
        return Response( content, status=status.HTTP_200_OK )
