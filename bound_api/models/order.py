from django.db import models


class Order(models.Model):
    # start_date_time	 = models.DateTimeField(blank=True)
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
    from_whow_id     = models.IntegerField(blank=True, null=True)
    for_whow_id      = models.IntegerField(blank=True, null=True)
