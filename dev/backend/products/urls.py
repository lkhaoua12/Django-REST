from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListCreateView.as_view()),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='products-detail'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='products-update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view()),
]