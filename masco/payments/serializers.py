# payments/serializers.py
import uuid
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

    def create(self, validated_data):
        # Auto-set reference and user
        validated_data["reference"] = str(uuid.uuid4()).replace("-", "").upper()
        validated_data["user"] = self.context["request"].user
        # Default status
        validated_data["status"] = "pending"
        return super().create(validated_data)

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero")
        return value