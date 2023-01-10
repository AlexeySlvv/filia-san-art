from django.shortcuts import render
from .models import SeasonModel, DirectoryModel


def season_list(request):
    return render(request, "app_anything/season_list.html", context={
        "seasons": SeasonModel.objects.all(),
    })


def season_detail(request, season):
    return render(request, "app_anything/season_detail.html", context={
        "season_name": season,
        "directories": DirectoryModel.objects.filter(season__name=season),
    })