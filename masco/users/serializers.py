# users/serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Address

User = get_user_model()


# -----------------------------------
# User Serializer (Profile / Read)
# -----------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']


# -----------------------------------
# User Registration Serializer
# -----------------------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],  # email used as username
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_active=True
        )

        # Generate JWT tokens immediately
        refresh = RefreshToken.for_user(user)
        self.token_data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return user


# # -----------------------------------
# # Email Login Serializer (JWT) ✅ FIXED SAFELY
# # -----------------------------------
# class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
#     username_field = "email"

#     def validate(self, attrs):
#         """
#         Map email -> username so Django authentication works
#         without changing your User model or views.
#         """

#         # Convert email into username internally
#         attrs["username"] = attrs.get("email")

#         # Run normal SimpleJWT validation
#         data = super().validate(attrs)

#         # Attach user info to response
#         user = self.user
#         data["user"] = {
#             "id": user.id,
#             "email": user.email,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#         }

#         return data


from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # Authenticate manually using username=email
        user = authenticate(
            username=email,
            password=password
        )

        if user is None:
            raise serializers.ValidationError(
                "Invalid email or password"
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "User account is disabled"
            )

        # Generate tokens using parent logic
        refresh = self.get_token(user)

        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        }

        return data



# class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         email = attrs.get("email")
#         password = attrs.get("password")

#         user = authenticate(username=email, password=password)

#         if user is None:
#             raise serializers.ValidationError("Invalid email or password")

#         if not user.is_active:
#             raise serializers.ValidationError("User account is disabled")

#         refresh = self.get_token(user)

#         return {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#             "user": {
#                 "id": user.id,
#                 "email": user.email,
#                 "first_name": user.first_name,
#                 "last_name": user.last_name,
#             }
#         }
#  updating
# -----------------------------------
# Address Serializer
# -----------------------------------
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'user',
            'address_line1',
            'address_line2',
            'city',
            'state',
            'country',
            'postal_code',
            'is_default'
        ]
        read_only_fields = ['user']


