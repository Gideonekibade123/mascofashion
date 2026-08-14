
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
# from django_rest_passwordreset.signals import reset_password_token_created


# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

# #     email_plaintext_message = f"""
# # Use the link below to reset your password:

# # {settings.FRONTEND_URL}/reset-password/{reset_password_token.key}
# # """

#  email_plaintext_message = f"""
# Hi {reset_password_token.user.first_name or 'there'},

# You requested a password reset for your MascoFashion account.

# Click the link below to reset your password:
# {settings.FRONTEND_URL}/reset-password/{reset_password_token.key}

# This link will expire shortly. If you did not request this, ignore this email.

# — The MascoFashion Team
# """
# send_mail(
#         "Password Reset for Masco Fashion",
#         email_plaintext_message,
#         settings.DEFAULT_FROM_EMAIL,
#         [reset_password_token.user.email],
#     )


from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = f"""
Hi {reset_password_token.user.first_name or 'there'},

You requested a password reset for your MascoFashion account.

Click the link below to reset your password:
{settings.FRONTEND_URL}/reset-password/{reset_password_token.key}

This link will expire shortly. If you did not request this, ignore this email.

— The MascoFashion Team
"""

    send_mail(
        "Password Reset for Masco Fashion",
        email_plaintext_message,
        settings.DEFAULT_FROM_EMAIL,
        [reset_password_token.user.email],
    )