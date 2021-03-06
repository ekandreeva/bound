"""bound URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('bound_api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('admin/', admin.site.urls),
    path('bound_api/', include('bound_api.urls', namespace='api')),
    path('customer_app/', include('customer_app.urls', namespace='customer_app')),
    path('driver_app/', include('driver_app.urls', namespace='driver_app')),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
]
