from django.urls import path
from app_shop import views
app_name = 'app_shop'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<pk>/', views.ProductDetails.as_view(), name='product_details')
]
