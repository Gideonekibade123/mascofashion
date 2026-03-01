# from django.contrib import admin 
# from django.urls import path, include
# from django.conf.urls.static import static
# from masco.masco import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/shop/', include('shop.urls')),  # <-- all shop APIs
#     path('api/users/', include('users.urls')),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shop/', include('shop.urls')),  # <-- all shop APIs
    path('api/users/', include('users.urls')), # user APIs
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
