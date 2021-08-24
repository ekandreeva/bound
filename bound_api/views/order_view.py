from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics

from bound_api.models import Order
from bound_api.serializers import OrderSerializer


class OrderList(generics.ListAPIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetail(generics.RetrieveAPIView):
    def get(self, request, order_id, format=None):
        order = Order.objects.get(pk=order_id)
        try:
            serializer = OrderSerializer(order, many=False)
            response = serializer.data
        except Order.DoesNotExist:
            response = {
                "error": "User is not bounder."
            }
            # raise Http404

        return Response(response)
