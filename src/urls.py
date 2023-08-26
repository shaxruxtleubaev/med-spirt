from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings.base import MEDIA_ROOT, MEDIA_URL
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/', include('app.urls')),

    # API simple-jwt
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns = [*i18n_patterns(*urlpatterns, prefix_default_language=False)]