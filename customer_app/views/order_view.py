from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework import viewsets
from rest_framework.decorators import action

from bound_api.models import User
from bound_api.models import Order
from bound_api.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    @action(detail=True, methods=['put'], url_path='charge_order')
    def charge_order(self, request, pk):
        order = Order.objects.first()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


    def get_object(self, request, pk):
        try:
            return request.user.order_set.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def list(self, request):
        user = request.user
        orders = user.order_set.all()
        serializer = OrderSerializer(orders, many=True)
        return Response( serializer.data, status=status.HTTP_200_OK )

    def create(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        order = self.get_object(request, pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk=None):
        order = self.get_object(request, pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        order = self.get_object(request, pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
