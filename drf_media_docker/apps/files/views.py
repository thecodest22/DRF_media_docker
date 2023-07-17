from rest_framework.viewsets import ReadOnlyModelViewSet

from project_common.permissions import IsSubscriber

from .models import File
from .serializers import FileSerializer


class FileViewSet(ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsSubscriber]
