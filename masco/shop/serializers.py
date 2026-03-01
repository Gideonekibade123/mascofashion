from rest_framework import serializers
from .models import (
    Category,
    Product,
    ProductImage,
    Review,
    Enquiry,
    Cart,
)


# ----------------------------
# Category
# ----------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
        ]


# ----------------------------
# Product Images
# ----------------------------
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'image',
        ]


# ----------------------------
# Reviews
# ----------------------------
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'rating',
            'comment',
            'created_at',
        ]


# ----------------------------
# Products (READ)
# ----------------------------
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'category',
            'price',
            'description',
            'stock',
            'is_active',
            'images',
            'reviews',
            'created_at',
        ]


# ----------------------------
# Products (CREATE / UPDATE)
# ----------------------------
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'price',
            'description',
            'stock',
            'is_active',
        ]


# ----------------------------
# Cart
# ----------------------------
class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'product',
            'quantity',
            'created_at',
        ]
        read_only_fields = ['user']


# ----------------------------
# Enquiries
# ----------------------------
class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = [
            'id',
            'name',
            'email',
            'message',
            'created_at',
        ]

