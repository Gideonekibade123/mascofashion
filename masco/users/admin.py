# Register your models here.
from django.contrib import admin
from .models import Address


# -----------------------------------
# Address Admin
# -----------------------------------
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'address_line1',
        'city',
        'state',
        'country',
        'is_default'
    )
    list_filter = ('country', 'state', 'is_default')
    search_fields = ('user__username', 'city', 'country')
