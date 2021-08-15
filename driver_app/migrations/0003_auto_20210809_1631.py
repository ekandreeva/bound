# Generated by Django 2.2 on 2021-08-09 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bound_api', '0011_auto_20210809_1441'),
        ('driver_app', '0002_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='OrdersDrivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver_app.Driver')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bound_api.Order')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='orders',
            field=models.ManyToManyField(related_name='drivers', through='driver_app.OrdersDrivers', to='bound_api.Order'),
        ),
    ]