"""sleepTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
# from rest_framework.urls import
from rest_framework.authtoken.views import obtain_auth_token
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', resgisterUser.as_view()),
    path('login/', obtain_auth_token, name='login'),
    path('storeSleep/', storeSleep.as_view(), name='storeSleep'),
    path('getSleep/<int:pk>', getSleep.as_view(), name='getSleep'),
    path('calculate/<str:ss>/<str:se>/', calculate, name='calculate'),
    path('logout/', logoutUser.as_view(), name='userLogout'),
]

# 2022-09-12T16:59
# YYYY-MM-DD HH:MM