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
        """
        Automatically generate a unique reference and assign the current user.
        Set status to 'pending' by default.
        """
        validated_data["reference"] = str(uuid.uuid4()).replace("-", "").upper()
        validated_data["user"] = self.context["request"].user
        validated_data["status"] = "pending"
        return super().create(validated_data)

    def validate_amount(self, value):
        """
        Ensure the amount is greater than zero.
        Store the amount in Naira (Paystack conversion to Kobo happens in the view).
        """
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero")
        return value