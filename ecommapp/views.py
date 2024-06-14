from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product
from .models import Customer

# Create your views here.

def home(request):
    return render(request, 'ecommapp/home.html')

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'ecommapp/productList.html', context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'ecommapp/productDetails.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'ecommapp/customerList.html', context)

def customer_details(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
        'customer': customer
    }
    return render(request, 'ecommapp/customerDetails.html', context)