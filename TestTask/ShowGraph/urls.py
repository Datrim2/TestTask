#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------
#/TestTask/ShowGraph/urls.py
#-------------------------------------------

from django.urls import path
from ShowGraph import views

app_name = 'showgraph'

urlpatterns = [
    path('load/',views.UploadFile.as_view(),name="load"),
    path('history/',views.HistoryList.as_view(),name="history"),
    path('plot/<int:files_id>/',views.index,name="plot"),
]