from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import action


from bound_api.models import User
from driver_app.models import Driver
from driver_app.serializers import DriverSerializer


class ApplicantList(generics.ListAPIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        applicants = Driver.objects.all()
        serializer = DriverSerializer(applicants, many=True)
        return Response(serializer.data)


class ApplicantViewSet(viewsets.ModelViewSet):

    @action(detail=True, methods=['put'])
    def accept_applicant(self, request, applicant_id):
        user = User.objects.get(pk=applicant_id)
        if user.type == 'DR':
            driver = user.driver
            driver.status='AC'
            driver.save()

            serializer = DriverSerializer(driver, many=False)
            response = serializer.data
        else:
            response = {
                "error": "User is not applicant."
            }

        return Response(response)

    @action(detail=True, methods=['put'])
    def decline_applicant(self, request, applicant_id):
        user = User.objects.get(pk=applicant_id)
        if user.type == 'DR':
            driver = user.driver
            driver.status='DC'
            driver.save()

            serializer = DriverSerializer(driver, many=False)
            response = serializer.data
        else:
            response = {
                "error": "User is not applicant."
            }

        return Response(response)
