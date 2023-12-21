from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static
from .views import product_detail


urlpatterns = [
    path('', views.main, name='home'),
    path('account/', include('users.urls')),
    path('<slug:slug>/', product_detail, name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)