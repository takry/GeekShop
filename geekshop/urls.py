
from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('products/', views.products),
    path('contact/', views.contact),

]
