# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from django.contrib.auth import get_user_model
# from rest_framework.authtoken.models import Token
# from django.core.mail import send_mail
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.shortcuts import get_object_or_404
# from django.conf import settings
# from rest_framework_simplejwt.views import TokenObtainPairView

# from .serializers import (
#     UserSerializer,
#     RegisterSerializer,
#     AddressSerializer,
#     EmailTokenObtainPairSerializer,
# )
# from .models import Address

# User = get_user_model()


# # -----------------------------------
# # Register View with Email Activation & JWT return
# # -----------------------------------
# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = [permissions.AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         # user = serializer.save()  # user is_active=True already

#         user = serializer.save()
#         user.is_active = False  # ← block login until email verified
#         user.save()

#         # Optional DRF token (not required for JWT)
#         Token.objects.get_or_create(user=user)

#         # Generate activation link (optional)
#         uid = urlsafe_base64_encode(force_bytes(user.pk))
#         token_email = default_token_generator.make_token(user)
#         frontend_activation_url = f"{settings.FRONTEND_URL}/activate/{uid}/{token_email}/"

#         send_mail(
#             subject="Activate your MascoFashion account",
#             message=f"Hi {user.first_name or 'there'}, click this link to activate your account:\n{frontend_activation_url}",
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[user.email],
#             fail_silently=False,
#         )


        
       


#         # headers = self.get_success_headers(serializer.data)

#         # # Return JWT tokens immediately for frontend login
#         # token_data = getattr(serializer, 'token_data', None)

#         # response_data = {
#         #     "user": serializer.data,
#         #     "message": "User registered successfully.",
#         # }

#         # if token_data:
#         #     response_data["tokens"] = token_data  # contains 'access' and 'refresh'

#         # return Response(
#         #     response_data,
#         #     status=status.HTTP_201_CREATED,
#         #     headers=headers,
#         # )


# headers = self.get_success_headers(serializer.data)

# response_data = {
#     "message": "Registration successful! Please check your email to activate your account.",
# }

# return Response(
#     response_data,
#     status=status.HTTP_201_CREATED,
#     headers=headers,
# )



# # -----------------------------------
# # Activation View
# # -----------------------------------
# class ActivateUserView(generics.GenericAPIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self, request, uidb64, token):
#         try:
#             uid = urlsafe_base64_decode(uidb64).decode()
#             user = get_object_or_404(User, pk=uid)
#         except (TypeError, ValueError, OverflowError):
#             return Response(
#                 {"error": "Invalid link"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         if default_token_generator.check_token(user, token):
#             user.is_active = True
#             user.save()
#             return Response(
#                 {"success": "Account activated"},
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return Response(
#                 {"error": "Invalid or expired token"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )


# # -----------------------------------
# # Email Login View (JWT)
# # -----------------------------------
# class EmailLoginView(TokenObtainPairView):
#     serializer_class = EmailTokenObtainPairSerializer


# # -----------------------------------
# # Profile View
# # -----------------------------------
# class ProfileView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self):
#         return self.request.user


# # -----------------------------------
# # List & Create Address
# # -----------------------------------
# class AddressListCreateView(generics.ListCreateAPIView):
#     serializer_class = AddressSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Address.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# # -----------------------------------
# # Update & Delete Address
# # -----------------------------------
# class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = AddressSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Address.objects.filter(user=self.request.user)





from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    UserSerializer,
    RegisterSerializer,
    AddressSerializer,
    EmailTokenObtainPairSerializer,
)
from .models import Address

User = get_user_model()


# -----------------------------------
# Register View with Email Activation & JWT return
# -----------------------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user.is_active = False
        user.save()

        Token.objects.get_or_create(user=user)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token_email = default_token_generator.make_token(user)
        frontend_activation_url = f"{settings.FRONTEND_URL}/activate/{uid}/{token_email}/"

        send_mail(
            subject="Activate your MascoFashion account",
            message=f"Hi {user.first_name or 'there'}, click this link to activate your account:\n{frontend_activation_url}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        headers = self.get_success_headers(serializer.data)

        response_data = {
            "message": "Registration successful! Please check your email to activate your account.",
        }

        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


# -----------------------------------
# Activation View
# -----------------------------------
class ActivateUserView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_object_or_404(User, pk=uid)
        except (TypeError, ValueError, OverflowError):
            return Response(
                {"error": "Invalid link"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response(
                {"success": "Account activated"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid or expired token"},
                status=status.HTTP_400_BAD_REQUEST,
            )


# -----------------------------------
# Email Login View (JWT)
# -----------------------------------
class EmailLoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


# -----------------------------------
# Profile View
# -----------------------------------
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# -----------------------------------
# List & Create Address
# -----------------------------------
class AddressListCreateView(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# -----------------------------------
# Update & Delete Address
# -----------------------------------
class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)