# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/shop/', include('masco.shop.urls')),  # all shop APIs
#     path('api/users/', include('masco.users.urls')), # user APIs
#     path('api/payments/', include('masco.payments.urls')),  # ✅ added payments APIs
#     path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
# ]

# # Serve media files in development
# # if settings.DEBUG:
# #     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shop/', include('masco.shop.urls')),
    path('api/users/', include('masco.users.urls')),
    path('api/payments/', include('masco.payments.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]