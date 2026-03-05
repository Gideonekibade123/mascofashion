# payments/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Payment
from .serializers import PaymentSerializer


class InitiatePaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        Create a new Payment instance and return details including
        amount in kobo (for Paystack).
        """
        serializer = PaymentSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()

        # Convert amount to kobo for Paystack
        amount_in_kobo = int(payment.amount * 100)

        return Response({
            "message": "Payment initiated",
            "payment": serializer.data,
            "amount_kobo": amount_in_kobo
        }, status=status.HTTP_201_CREATED)


class PaymentListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.filter(user=request.user).order_by("-created_at")
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PaymentDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, reference):
        try:
            payment = Payment.objects.get(reference=reference, user=request.user)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VerifyPaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        Manually verify a payment using its reference.
        """
        reference = request.data.get("reference")
        if not reference:
            return Response({"error": "Reference is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payment = Payment.objects.get(reference=reference, user=request.user)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

        # In production, you would call Paystack's API here to confirm payment
        payment.status = "successful"  # simulate success
        payment.save()

        serializer = PaymentSerializer(payment)
        return Response({"message": "Payment verified", "payment": serializer.data}, status=status.HTTP_200_OK)


class PaymentWebhookView(APIView):
    permission_classes = [permissions.AllowAny]  # Called by payment gateways

    def post(self, request):
        """
        Receive webhook events from Paystack or another provider.
        Update payment status based on incoming data.
        """
        data = request.data
        reference = data.get("reference")
        status_str = data.get("status")

        if not reference or not status_str:
            return Response({"error": "Invalid webhook data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payment = Payment.objects.get(reference=reference)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

        # Map gateway status to our model's status
        if status_str.lower() in ["success", "successful", "completed"]:
            payment.status = "successful"
        elif status_str.lower() in ["failed", "error"]:
            payment.status = "failed"
        else:
            payment.status = "pending"

        payment.save()
        return Response({"message": "Webhook processed"}, status=status.HTTP_200_OK)