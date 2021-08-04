from django.urls import re_path, include, path

from driver_app.views import RegistrationAPIView
from driver_app.views import LoginAPIView

app_name = 'driver_app'
urlpatterns = [
    re_path(r'^sign_up/?$', RegistrationAPIView.as_view(), name='driver_sign_up'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='driver_login'),
]
