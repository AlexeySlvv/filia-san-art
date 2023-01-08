from django.core.management.base import BaseCommand
from ...models import AnythingModel


class Command(BaseCommand):
    help = 'Fill Anything database'

    def handle(self, *args, **kwargs):
        pass
