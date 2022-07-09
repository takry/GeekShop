
from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/all/', views.products, name='products_all'),
    path('products/home/', views.products, name='products_home'),
    path('products/office/', views.products, name='products_office'),
    path('products/modern/', views.products, name='products_modern'),
    path('products/classic/', views.products, name='products_classic'),
    #path('products/<pk:int>/', views.products_category, name='products_all'),
    path('contact/', views.contact, name='contact'),

]
