from django.contrib import admin
from django.urls import path, include
from mainapp import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='authapp')),

    # path('products/<pk:int>/', views.products_category, name='products_all'),
    path('contact/', views.contact, name='contact'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
