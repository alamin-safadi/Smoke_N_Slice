from django.db import models
from django.contrib.auth.models import User
from menu.models import Item

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            import random
            import string
            self.order_number = 'SN' + ''.join(random.choices(string.digits, k=8))
        
        discount_amount = (self.total_amount * self.discount_percent) / 100
        self.final_amount = self.total_amount - discount_amount
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Order {self.order_number} - {self.staff.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    @property
    def subtotal(self):
        return self.quantity * self.price
    
    def __str__(self):
        return f"{self.quantity} x {self.item.name}"