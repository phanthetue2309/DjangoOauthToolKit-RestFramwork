from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):

    @property
    def get_scopes_with_actions(self):
        return f'{self.basename}:{self.action}'
