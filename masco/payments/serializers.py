# payments/serializers.py

from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "user",
            "amount",
            "reference",
            "status",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "reference",
            "status",
            "created_at",
        ]
