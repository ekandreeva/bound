from django.urls import re_path, include, path

from driver_app.views import RegistrationAPIView
from driver_app.views import LoginAPIView
from driver_app.views import DriverViewSet


app_name = 'driver_app'
urlpatterns = [
    re_path(r'^sign_up/?$', RegistrationAPIView.as_view(), name='driver_sign_up'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='driver_login'),
    path('update_profile/', DriverViewSet.as_view({'patch': 'update_profile'}), name='driver-update-profile'),
    path('add_vechicle/', DriverViewSet.as_view({'put': 'add_vechicle'}), name='driver-add-vechicle'),
    path('orders/', DriverViewSet.as_view({'get': 'orders'}), name='driver-orders'),
    path('accept_order/<int:order_id>/', DriverViewSet.as_view({'put': 'accept_order'}), name='driver-accept-order'),
    path('drop_order/<int:order_id>/', DriverViewSet.as_view({'put': 'drop_order'}), name='driver-drop-order'),
    path('pick_order/<int:order_id>/', DriverViewSet.as_view({'put': 'pick_order'}), name='driver-pick-order'),
    path('add_photo/', DriverViewSet.as_view({'put': 'add_photo'}), name='driver-add-photo'),
]
