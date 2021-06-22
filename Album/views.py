from api_base.views.base import BaseViewSet
from .models import Album
from .serializers import AlbumSerializer

from api_base.views.base import BaseViewSet
from api_base.permissions.token_permission import TokenPermissionWithAction


# Test Using ViewSet
class AlbumViewSet(BaseViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [TokenPermissionWithAction]

    def list(self, request, *args, **kwargs):
        return super(AlbumViewSet, self).list(request)
