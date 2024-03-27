from django.urls import path
from .views import api_rs
from rest_framework.authtoken import views

urlpatterns = [
    path('auth/', views.obtain_auth_token),
    path('', api_rs, name='api_rs')
]