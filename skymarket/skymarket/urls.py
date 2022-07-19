from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]

urlpatterns += [path("api/", SpectacularAPIView.as_view(), name='schema'),
                path("api/docs/", SpectacularSwaggerView.as_view(url_name='schema'))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [path("api/", include("users.urls"))]

# urlpatterns += [path('api/', include('djoser.urls'))]
# urlpatterns += [path('api/', include('djoser.urls.authtoken'))]
urlpatterns += [path('api/', include('ads.urls'))]
