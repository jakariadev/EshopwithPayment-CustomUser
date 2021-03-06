from django.urls import path
from app_order import views
app_name = 'app_order'

urlpatterns = [
    path('add/<pk>/', views.add_to_cart, name='order'),
    path('cart/', views.cartview, name='cart'),
    path('remove/<pk>/', views.remove_from_cart, name="remove"),
]
