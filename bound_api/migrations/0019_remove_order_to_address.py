# Generated by Django 2.2 on 2021-08-25 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bound_api', '0018_auto_20210825_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='to_address',
        ),
    ]
