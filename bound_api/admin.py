from django.contrib import admin
from .models import Order
from .models import User
from .models import Address
from .models import PaymentMethod
from .models import Payment
from customer_app.models import Customer
from driver_app.models import Driver


# Register your models here.
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Address)
admin.site.register(PaymentMethod)
admin.site.register(Payment)
