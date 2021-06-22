from django.urls import path, include
from django.contrib import admin
from . import api_router

admin.autodiscover()


# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include(api_router)),
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('accounts.urls')),
    # ...
]
