from django.contrib import admin
from .models import Category, Product, ProductImage, Review, Cart, Enquiry


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'is_active',
        'created_at',
    )
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Enquiry)

