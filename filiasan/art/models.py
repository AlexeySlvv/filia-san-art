from django.db import models


class ArtistModel(models.Model):
    name = models.CharField(max_length=1024, null=False)

    def __str__(self):
        return self.name


class ArtModel(models.Model):
    artist = models.ForeignKey(ArtistModel, null=False, on_delete=models.CASCADE)
    year = models.DateField(null=True, default=None)
    desc = models.TextField(default='', null=False)
    url = models.CharField(max_length=1024, null=False)
    orig_id = models.IntegerField(null=False)

    def __str__(self):
        return self.desc
