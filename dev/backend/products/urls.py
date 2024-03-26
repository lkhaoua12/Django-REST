from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductCreateView.as_view()),
    path('<int:pk>/', views.ProductDetailView.as_view()),
]