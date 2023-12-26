from django.urls import path, include

from cart.views import view_cart, add_to_cart, update_cart, remove_from_cart, increment_cart, decrement_cart
from main import views
from django.conf import settings
from django.conf.urls.static import static
from .views import product_detail, about, contacts

urlpatterns = [
    path('', views.main, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('account/', include('users.urls')),
    path('view_cart/', view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:cart_id>/', update_cart, name='update_cart'),
    path('remove_from_cart/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('increment_cart/<int:cart_id>/', increment_cart, name='increment_cart'),
    path('decrement_cart/<int:cart_id>/', decrement_cart, name='decrement_cart'),
    path('<slug:slug>/', product_detail, name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)