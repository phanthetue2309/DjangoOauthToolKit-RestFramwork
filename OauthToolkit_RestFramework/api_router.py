from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from Album.views import AlbumViewSet
from Instrument.views import InstrumentViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('album', AlbumViewSet, basename='album')
router.register('instrument', InstrumentViewSet, basename='instrument')

app_name = 'api'
urlpatterns = router.urls
