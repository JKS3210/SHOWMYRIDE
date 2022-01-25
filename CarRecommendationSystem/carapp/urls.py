from django.urls import path
import carapp.views

urlpatterns = [
    path('',carapp.views.home,name="home"),
    path('index/',carapp.views.index,name="index"),
    path('about/', carapp.views.about, name="about"),
    path('viewres',carapp.views.viewres,name="viewres")
]