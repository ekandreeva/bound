# Generated by Django 2.2 on 2021-08-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_items', models.PositiveIntegerField(default=0)),
                ('sender', models.CharField(max_length=255)),
                ('recipient', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('accepted_at', models.DateTimeField(blank=True, null=True)),
                ('picked_at', models.DateTimeField(blank=True, null=True)),
                ('droped_at', models.DateTimeField(blank=True, null=True)),
                ('destination_type', models.CharField(max_length=255, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('from_whow_id', models.IntegerField(blank=True, null=True)),
                ('for_whow_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('zipcode', models.CharField(blank=True, max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('type', models.CharField(choices=[('AD', 'Admin'), ('DR', 'Driver'), ('CU', 'Customer')], default='CU', max_length=255)),
                ('username', models.CharField(blank=True, max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
