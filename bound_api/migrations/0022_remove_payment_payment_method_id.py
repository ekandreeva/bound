# Generated by Django 2.2 on 2021-08-26 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bound_api', '0021_auto_20210825_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_method_id',
        ),
    ]