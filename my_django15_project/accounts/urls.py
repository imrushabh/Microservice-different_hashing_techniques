from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^register$',views.register),
]
