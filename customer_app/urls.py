from django.urls import re_path, include, path

from customer_app import views
from customer_app.views import RegistrationAPIView
from customer_app.views import LoginAPIView
# from customer_app.views import OrderViewSet, OrderList, OrderDetail
from customer_app.views import OrderViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet)



order_charge_order = OrderViewSet.as_view({'put': 'charge_order'})

app_name = 'customer_app'
urlpatterns = [
    re_path(r'^sign_up/?$', RegistrationAPIView.as_view(), name='customer_sign_up'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='customer_login'),
    path('', include(router.urls)),
    path('orders/<int:pk>/charge_order/', order_charge_order, name='order-charge-order'),
]
