# from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import (
#     RegisterView,
#     ProfileView,
#     AddressListCreateView,
#     AddressDetailView,
#     ActivateUserView,
# )

# urlpatterns = [
#     # Auth
#     path('signup/', RegisterView.as_view(), name='signup'),
#     path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name='activate'),  # email activation
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # <-- fixed
#     path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('profile/', ProfileView.as_view(), name='profile'),

#     # Addresses
#     path('addresses/', AddressListCreateView.as_view(), name='address-list'),
#     path('addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
# ]




# from django.urls import path
# from rest_framework_simplejwt.views import TokenRefreshView
# from .views import (
#     RegisterView,
#     ProfileView,
#     AddressListCreateView,
#     AddressDetailView,
#     ActivateUserView,
#     EmailLoginView,   # important
# )

# urlpatterns = [
#     # Auth
#     path('signup/', RegisterView.as_view(), name='signup'),
#     path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name='activate'),
#     path('login/', EmailLoginView.as_view(), name='token_obtain_pair'),  # ✅ FIXED
#     path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('profile/', ProfileView.as_view(), name='profile'),

#     # Addresses
#     path('addresses/', AddressListCreateView.as_view(), name='address-list'),
#     path('addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
# ]


from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    ActivateUserView,
    EmailLoginView,
    ProfileView,
    AddressListCreateView,
    AddressDetailView,
)

urlpatterns = [
    # --------------------
    # Authentication
    # --------------------
    path('signup/', RegisterView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name='activate'),
    path('login/', EmailLoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # --------------------
    # Addresses
    # --------------------
    path('addresses/', AddressListCreateView.as_view(), name='address-list'),
    path('addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
]