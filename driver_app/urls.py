from django.urls import re_path, include, path

from driver_app.views import RegistrationAPIView
from driver_app.views import LoginAPIView
from driver_app.views import DriverViewSet


# driver_update_profile = DriverViewSet.as_view({'put': 'update_profile'})

app_name = 'driver_app'
urlpatterns = [
    re_path(r'^sign_up/?$', RegistrationAPIView.as_view(), name='driver_sign_up'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='driver_login'),
    # path('update_profile/', driver_update_profile, name='driver-update-profile'),

]
