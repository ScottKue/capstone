from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.showEntry, name="showEntry"),
   path("<str:title>", views.showEntry, name="showEntry"),
 path("Place1", views.showEntry, name='Place1')
]
