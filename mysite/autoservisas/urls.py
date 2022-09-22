from django.contrib import admin
from django.urls import include, path
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
 path('', views.index, name='index'),
 path('automobiliai/', views.automobiliai, name='autos'),
 # path('uzsakymu_sarasas/', UzsakListView.as_view(), name= "")
]
