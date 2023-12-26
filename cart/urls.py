from django.urls import path
from .views import view_cart, add_to_cart, update_cart, remove_from_cart

urlpatterns = [
    path('view_cart/', view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:cart_id>/', update_cart, name='update_cart'),
    path('remove_from_cart/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
]