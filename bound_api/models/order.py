from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .user import User
from .address import Address
from .orders_users import OrdersUsers


class Order(models.Model):
    start_date_time	 = models.DateTimeField(blank=True, null=True)
    number_of_items  = models.PositiveIntegerField(default=0)
    sender           = models.CharField(max_length=255)
    recipient        = models.CharField(max_length=255)
    status           = models.CharField(max_length=255)
    accepted_at      = models.DateTimeField(blank=True, null=True)
    picked_at        = models.DateTimeField(blank=True, null=True)
    droped_at        = models.DateTimeField(blank=True, null=True)
    destination_type = models.CharField(max_length=255, null=True)
    contact_email    = models.EmailField(blank=True, null=True)
    contact_phone    = models.CharField(max_length=255, blank=True, null=True)
    note             = models.TextField(blank=True, null=True)
    type             = models.CharField(max_length=255, blank=True, null=True)
    user             = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='orders')
    from_whom        = models.ForeignKey(OrdersUsers, on_delete=models.CASCADE, blank=True, null=True, related_name='from_whom_order')
    for_whom         = models.ForeignKey(OrdersUsers, on_delete=models.CASCADE, blank=True, null=True, related_name='for_whom_order')
    from_address     = GenericRelation(Address)
    to_address       = GenericRelation(Address)


    def __str__(self):
        return str(self.id)

    def driver(self):
        return self.drivers.orders_drivers.filter(accepted=True)
