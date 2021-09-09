from django.urls import path
from app_order import views
app_name = 'app_order'

urlpatterns = [
    path('<pk>/', views.add_to_cart, name='order'),
]