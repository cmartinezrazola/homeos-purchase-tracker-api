from django.db import models
from django.utils import timezone

class Marketplace(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.PROTECT, related_name='orders')
    shop = models.CharField(max_length=255)
    shipping = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order #{self.id} - {self.marketplace.name} (Shop: {self.shop})'

class OrderItem(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    # specs = models.JSONField(blank=True, null=True)
    specs = models.CharField(max_length=255)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')

    def __str__(self):
        if self.brand:
            return f'{self.name} ({self.brand})'
        return self.name
