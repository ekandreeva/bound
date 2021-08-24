from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics

from bound_api.models import User
from customer_app.models import Customer
from customer_app.serializers import CustomerSerializer


class BounderList(generics.ListAPIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        bounders = Customer.objects.all()
        serializer = CustomerSerializer(bounders, many=True)
        return Response(serializer.data)


class BounderDetail(generics.RetrieveAPIView):
    def get(self, request, bounder_id, format=None):
        user = User.objects.get(pk=bounder_id)
        if user.type == 'CU':
            serializer = CustomerSerializer(user.customer, many=False)
            response = serializer.data
        else:
            response = {
                "error": "User is not bounder."
            }

        return Response(response)
