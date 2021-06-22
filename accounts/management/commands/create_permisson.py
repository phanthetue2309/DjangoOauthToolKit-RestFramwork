from django.core.management.base import BaseCommand

from accounts.models import Permission
from accounts.ultis import get_api_actions


class Command(BaseCommand):
    help = "Create permissions with url pattern"

    def handle(self, *args, **kwargs):
        for scope in get_api_actions():
            '''
            Example of scope: album:create
            '''
            name_scope = scope.split(':')
            basename = name_scope[0].replace('_', ' ')  # name of scope: album
            action_name = name_scope[1].replace('_', ' ')   # name of action: create
            Permission.objects.get_or_create(
                scope=scope,
                description=f'{action_name.title()} object of {basename.title()}'
            )
        self.stdout.write(self.style.SUCCESS('Successfully create permissions'))