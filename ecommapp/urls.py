from django.urls import path
from . import views

app_name = 'ecommapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_details, name='product_details'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>', views.customer_details, name='customer_details')
]