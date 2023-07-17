from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostViewSet
from apps.videos.views import VideoViewSet
from apps.files.views import FileViewSet


schema_view = get_swagger_view(title='Test API')
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'videos', VideoViewSet, basename='video')
router.register(r'files', FileViewSet, basename='file')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
