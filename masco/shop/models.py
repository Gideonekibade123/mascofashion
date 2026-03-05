from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import JSONField

User = get_user_model()


# ============================
# Category
# ============================
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# ============================
# Product
# ============================
SIZES_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
)

COLOR_CHOICES = (
    ('RED', 'Red'),
    ('BLUE', 'Blue'),
    ('BLACK', 'Black'),
    ('WHITE', 'White'),
    ('GREEN', 'Green'),
    ('YELLOW', 'Yellow'),
    ('ORANGE', 'Orange'),
    ('PURPLE', 'Purple'),
    ('PINK', 'Pink'),
    ('BROWN', 'Brown'),
    ('GRAY', 'Gray'),
)


class Product(models.Model):
    SIZES = models.CharField(max_length=5, choices=SIZES_CHOICES)
    COLOR = models.CharField(max_length=10, choices=COLOR_CHOICES)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ============================
# Product Images
# ============================
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"


# ============================
# Review
# ============================
class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} review on {self.product.name}"


# ============================
# Cart
# ============================
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.user}"


# ============================
# Enquiry
# ============================
class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.name}"
    
    # ============================
# Order
# ============================
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Billing Details
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    billing_address = models.TextField()

    # Shipping Address
    shipping_address = models.TextField()

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user}"
