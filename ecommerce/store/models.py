from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    name         = models.CharField(max_length=200)
    slug         = models.SlugField(unique=True)
    description  = models.TextField(blank=True)
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image        = models.ImageField(upload_to='products/', blank=True)
    stock        = models.IntegerField(default=0)
    available    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = [
        ('pending',    'Pending'),
        ('processing', 'Processing'),
        ('shipped',    'Shipped'),
        ('delivered',  'Delivered'),
        ('cancelled',  'Cancelled'),
    ]

    PAYMENT_CHOICES = [
        ('upi',        'UPI / GPay'),
        ('card',       'Credit / Debit Card'),
        ('netbanking', 'Net Banking'),
        ('cod',        'Cash on Delivery'),
    ]

    user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cod')
    total_amount   = models.DecimalField(max_digits=10, decimal_places=2)
    address        = models.TextField(blank=True)
    city           = models.CharField(max_length=100, blank=True)
    state          = models.CharField(max_length=100, blank=True)
    pincode        = models.CharField(max_length=10, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order #{self.id} by {self.user.username}'


class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price    = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_total(self):
        return self.price * self.quantity