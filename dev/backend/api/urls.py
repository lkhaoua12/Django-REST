from django.urls import path
from .views import api_rs

urlpatterns = [
    path('', api_rs, name='api_rs')
]