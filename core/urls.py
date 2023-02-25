from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home_view, name='home'),
]
