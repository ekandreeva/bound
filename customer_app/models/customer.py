from django.db import models
from bound_api.models import User


class Customer(models.Model):
    stripe_id = models.CharField(max_length=255, null=True)
    user      = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
