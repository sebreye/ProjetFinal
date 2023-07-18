from django.db import models
from users.models import Users
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Products(models.Model):
    GENDER_CHOICES = (
        ('M', 'Homme'),
        ('F', 'Femme'),
        ('U', 'Unisexe'),
    )

    DISCOUNT_CHOICES = (
        (0, 'Pas de promo'),
        (25, '25% de réduction'),
        (40, '40% de réduction'),
        (50, '50% de réduction'),
    )

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image1 = models.URLField()
    image2 = models.URLField()
    image3 = models.URLField()
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    description = models.TextField()
    discount = models.IntegerField(choices=DISCOUNT_CHOICES, default=0)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    def reduce_stock(self, quantity=1):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()




class CartItem(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.product.price * self.quantity

class CommentaryProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.name}"

# class wishlist(models.Model):
