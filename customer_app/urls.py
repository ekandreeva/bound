from django.urls import re_path, include, path
from bound_api.router import router

from bound_api.views import RegistrationAPIView
from bound_api.views import LoginAPIView

app_name = 'customer_app'
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^sign_up/?$', RegistrationAPIView.as_view(), name='customer_sign_up'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='customer_login'),
]
