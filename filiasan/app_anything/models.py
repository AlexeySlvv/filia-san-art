from django.db import models


class AnythingModel(models.Model):
    directory = models.CharField(max_length=256, null=False)
    prompt = models.CharField(max_length=1000, null=False)
    season = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.prompt
