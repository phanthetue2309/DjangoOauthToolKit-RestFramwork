from rest_framework.permissions import BasePermission
import logging

from api_base.views.base import BaseViewSet

log = logging.getLogger("oauth2_provider")


class TokenPermissionWithAction(BasePermission):

    def has_permission(self, request, view):
        token = request.auth

        if not token:
            return False

        if hasattr(token, "scope"):  # OAuth 2

            view: BaseViewSet = view
            scope = view.get_scopes_with_actions
            m = request.method.upper()
            required_scopes = {
                m: [[scope]]
            }
            for alt in required_scopes[m]:
                if token.is_valid(alt):
                    print("check")
                    return True
            return False

        assert False, (
            "TokenRequirements requires the"
            "`oauth2_provider.rest_framework.OAuth2Authentication` authentication "
            "class to be used."
        )


