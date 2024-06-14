from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"