from django.db import models
from django.conf import settings # To get AUTH_USER_MODEL
from products.models import Product # Assuming products app is correctly defined

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.email}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'product') # A user can only have one of each product in their cart

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart.user.email}'s cart"

    @property
    def total_price(self):
        return self.quantity * self.product.price