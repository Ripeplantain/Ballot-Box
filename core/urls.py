from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home_view, name='home'),
    path('election/<int:id>',election_view, name='election'),
    path('vote/<int:id>',vote_view, name='vote'),
    path('results/',results_view, name='results'),
    path('box/<int:id>/',box_view, name='box'),
]
