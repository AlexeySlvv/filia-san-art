from django.core.management.base import BaseCommand
from ...models import ArtModel, ArtistModel

class Command(BaseCommand):
    help = 'Clear art database'

    def handle(self, *args, **kwargs):
        ArtModel.objects.all().delete()
        ArtistModel.objects.all().delete()
