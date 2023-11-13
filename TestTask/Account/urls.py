#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------
#/TestTask/ShowGraph/urls.py
#-------------------------------------------

from django.urls import path
from Account import views

app_name = 'account'

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
]