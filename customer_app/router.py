from customer_app.viewsets import OrderViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
