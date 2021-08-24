from django.urls import re_path, include, path

from driver_app.views import RegistrationAPIView
from driver_app.views import LoginAPIView
from driver_app.views import DriverViewSet


driver_update_profile = DriverViewSet.as_view({'put': 'update_profile'})
driver_add_vechicle = DriverViewSet.as_view({'put': 'add_vechicle'})
driver_orders = DriverViewSet.as_view({'get': 'orders'})
driver_accept_order = DriverViewSet.as_view({'put': 'accept_order'})

app_name = 'driver_app'
urlpatterns = [
    re_path(r'^sign_up/?$', RegistrationAPIView.as_view(), name='driver_sign_up'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='driver_login'),
    path('update_profile/', driver_update_profile, name='driver-update-profile'),
    path('add_vechicle/', driver_add_vechicle, name='driver-add-vechicle'),
    path('orders/', driver_orders, name='driver-orders'),
    path('accept_order/<int:order_id>', driver_accept_order, name='driver-accept-order'),
]
