from django.urls import path

from .views import Index

urlpatterns = [
    path('data/', Index.as_view(), name='index'),
]