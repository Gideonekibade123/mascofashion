# payments/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Payment
from .serializers import PaymentSerializer


class InitiatePaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PaymentSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        return Response({
            "message": "Payment initiated",
            "payment": serializer.data
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
        # This endpoint can be used for manual verification
        reference = request.data.get("reference")
        if not reference:
            return Response({"error": "Reference is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payment = Payment.objects.get(reference=reference, user=request.user)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

        # Example: mark as completed (replace with real gateway check)
        payment.status = "completed"
        payment.save()

        serializer = PaymentSerializer(payment)
        return Response({"message": "Payment verified", "payment": serializer.data}, status=status.HTTP_200_OK)


class PaymentWebhookView(APIView):
    permission_classes = [permissions.AllowAny]  # Payment gateways call this

    def post(self, request):
        # Handle webhook data from the payment provider
        data = request.data
        reference = data.get("reference")
        status_str = data.get("status")

        if not reference or not status_str:
            return Response({"error": "Invalid webhook data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payment = Payment.objects.get(reference=reference)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update payment status based on gateway
        payment.status = status_str
        payment.save()

        return Response({"message": "Webhook processed"}, status=status.HTTP_200_OK)