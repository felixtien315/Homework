from django.urls import path
from . import views

app_name = 'nightmarket'

urlpatterns = [
    path('', views.food_list, name='food_list'),
]