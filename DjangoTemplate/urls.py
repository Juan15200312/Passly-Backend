from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView
from decouple import config
from DjangoTemplate import settings

admin.site.index_title = "Bienvenido"
admin.site.site_header = "Administración"
admin.site.site_title = f"Panel {config('SITE_TITLE')}"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Users.urls')),
    path('api/', include('Passwords.urls')),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
