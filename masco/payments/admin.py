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
        "updated_at",  # now exists on model
    )
    list_filter = ("status", "created_at")
    search_fields = ("reference", "user__username", "user__email")
    ordering = ("-created_at",)
    readonly_fields = ("reference", "created_at", "updated_at")
    list_editable = ("status",)  # edit status directly from list view