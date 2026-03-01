# from django.shortcuts import render

# # Create your views here.


# # payments/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Payment
# import uuid

# class InitiatePaymentView(APIView):
#     def post(self, request):
#         user = request.user
#         amount = request.data.get('amount')

#         reference = str(uuid.uuid4())

#         payment = Payment.objects.create(
#             user=user,
#             amount=amount,
#             reference=reference,
#             status='pending'
#         )

#         return Response({
#             "message": "Payment initiated",
#             "reference": reference,
#             "amount": amount
#         }, status=status.HTTP_201_CREATED)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
import uuid

class InitiatePaymentView(APIView):
    def post(self, request):
        user = request.user

        if not user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        amount = request.data.get('amount')
        if not amount:
            return Response({"error": "Amount is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amount = int(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero")
        except ValueError:
            return Response({"error": "Amount must be a positive integer"}, status=status.HTTP_400_BAD_REQUEST)

        reference = str(uuid.uuid4())

        payment = Payment.objects.create(
            user=user,
            amount=amount,  # store in Kobo for Paystack
            reference=reference,
            status='pending'
        )

        return Response({
            "message": "Payment initiated",
            "reference": reference,
            "amount": amount
        }, status=status.HTTP_201_CREATED)

