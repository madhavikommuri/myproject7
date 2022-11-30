from django.urls import path
from app2.views import *
app_name='ms'

urlpatterns=[
    path('meghana/',meghana,name='meghana'),
]