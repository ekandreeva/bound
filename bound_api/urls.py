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
from django.urls import re_path, include, path
from bound_api.router import router

from bound_api.views import RegistrationAPIView
from bound_api.views import LoginAPIView

app_name = 'bound_api'
urlpatterns = [
    # path('', include(router.urls)),
    re_path(r'^sign_up/?$', RegistrationAPIView.as_view(), name='user_sign_up'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]
