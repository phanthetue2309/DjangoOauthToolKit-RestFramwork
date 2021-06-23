import json

from django.http import HttpResponse
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import app_authorized
from oauth2_provider.views.mixins import OAuthLibMixin
from django.views.generic import View
from django.utils.decorators import method_decorator


class TokenView(OAuthLibMixin, View):

    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        pass
