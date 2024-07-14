from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.showallproduct,name='showllproduct'),
    path('product/<int:pk>/',views.productdetail,name='product'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('updateproduct/<int:pk>/',views.updateProduct,name='updateproduct'),
    path('deleteproduct/<int:pk>/',views.deleteproduct,name='deleteproduct'),
    
]