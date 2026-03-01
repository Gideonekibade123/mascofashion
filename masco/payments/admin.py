from django.contrib import admin

# Register your models here.
# payments/admin.py

from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "amount",
        "reference",
        "status",
        "created_at",
    )
    list_filter = ("status", "created_at")
    search_fields = ("reference", "user__username", "user__email")
    ordering = ("-created_at",)
    readonly_fields = ("reference", "created_at")
