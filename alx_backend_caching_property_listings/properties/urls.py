from django.urls import path
from .views import property_list
from .views import cache_metrics_view

urlpatterns = [
    path('', property_list, name='property_list'),
    path('metrics/', cache_metrics_view, name='cache_metrics'),
]