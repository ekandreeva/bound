from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from bound.permission import CustomerOnly
from bound_api.models import User
from bound_api.models import Order
from bound_api.serializers import OrderSerializer, UserSerializer, PaymentMethodSerializer, PaymentSerializer
import stripe
stripe.api_key = 'sk_test_51JScrnBVO6fSdtX9k02OjcY01KcYTiO6VeJVYzldHnnR3bWKGsyIDGWtQV6OgsIJ2cwj2M63VrBD7e4HpkAQmxb600R2UGRoH2'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomerOnly]

    @action(detail=True, methods=['put'], url_path='charge_order')
    def charge_order(self, request, pk):
        user = request.user

        stripe_user = stripe.Customer.create(
            email=user.email
        )

        user.customer.stripe_id = stripe_user.id
        user.customer.save()

        card = stripe.Customer.create_source(
          user.customer.stripe_id,
          source="tok_mastercard",
        )
        pm_info = {
            'user': user.id,
            'stripe_id': card.id,
            'last_4': request.data['last_4'],
            'exp_date': request.data['exp_date']
        }

        pm = PaymentMethodSerializer(data=pm_info)
        if pm.is_valid():
            pm.save()

        stripe_payment = stripe.Charge.create(
          amount=request.data['amount'],
          currency="usd",
          source='tok_mastercard'
        )
        order = self.get_object(request, pk)

        payment_info = {
            'order': order.id,
            'payment_method': pm.data,
            'stripe_charge_id': stripe_payment.id,
            'amount': request.data['amount'],
        }

        payment = PaymentSerializer(data=payment_info)
        if payment.is_valid():
            payment.save()

        return Response(payment.data)

    def get_object(self, request, pk):
        try:
            return request.user.orders.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def list(self, request):
        user = request.user
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response( serializer.data, status=status.HTTP_200_OK )

    def create(self, request):
        data = request.data
        user = request.user
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            order = serializer.save()
            user.orders.add(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        order = self.get_object(request, pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk=None):
        order = self.get_object(request, pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        order = self.get_object(request, pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
