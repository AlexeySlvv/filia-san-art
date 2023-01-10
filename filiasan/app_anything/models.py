from django.db import models


class SeasonModel(models.Model):
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name


class DirectoryModel(models.Model):
    name = models.CharField(max_length=256, null=False)
    prompt = models.CharField(max_length=1000, null=False)
    season = models.ForeignKey(SeasonModel, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.prompt


class AnythingModel(models.Model):
    directory = models.ForeignKey(DirectoryModel, null=False, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.image_name
