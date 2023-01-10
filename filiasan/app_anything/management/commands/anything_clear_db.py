from django.core.management.base import BaseCommand
from ...models import SeasonModel, DirectoryModel, AnythingModel


class Command(BaseCommand):
    help = 'Clear anything database'

    def handle(self, *args, **kwargs):
        AnythingModel.objects.all().delete()
        DirectoryModel.objects.all().delete()
        SeasonModel.objects.all().delete()
