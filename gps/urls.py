from django.urls import path

from .views import DataView, GpsView

urlpatterns = [
    path('gps/', GpsView.as_view(), name='Gps'),
    path('data/', DataView.as_view(), name='Data'),
]