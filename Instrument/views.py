from django.http import JsonResponse
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.decorators import action
from .models import Instrument
from .serializers import InstrumentSerializer

from api_base.views.base import BaseViewSet
from api_base.permissions.token_permission import TokenPermissionWithAction


# Test Using ViewSet - using TokenMatchesOASRequirements
class InstrumentViewSet(BaseViewSet):
    authentication_classes = [OAuth2Authentication]
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [TokenPermissionWithAction]

    @action(methods=["get"], detail=False)
    def response_test(self, request):
        data = {
            'msg': "Response Test Success"
        }
        return JsonResponse(data)

    # @action(methods=["get"], detail=True, url_path='response-test2')
    # def response_test2(self, request, pk):
    #     token = request.auth
    #     required_scopes = {
    #         "GET": [["instruments:response"]]
    #     }
    #     if not token:
    #         data = {
    #             'msg': "No scope provide"
    #         }
    #         return JsonResponse(data)
    #
    #     for alt in required_scopes["GET"]:
    #         if token.is_valid(alt):
    #             data = {
    #                 'msg': "Success"
    #             }
    #             return JsonResponse(data)
    #
    #     data = {
    #         'msg': "You do not have this permission"
    #     }
    #     return JsonResponse(data)
