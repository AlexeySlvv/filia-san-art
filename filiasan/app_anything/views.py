from django.shortcuts import render
from .models import SeasonModel, DirectoryModel, AnythingModel


def season_list(request):
    return render(request, "app_anything/season_list.html", context={
        "seasons": SeasonModel.objects.all().order_by("order"),
    })


def season_detail(request, season):
    return render(request, "app_anything/season_detail.html", context={
        "season_name": season,
        "directories": DirectoryModel.objects.filter(season__name=season).order_by("prompt"),
    })


def directory_detail(request, season, directory):
    dir = DirectoryModel.objects.filter(name=directory).first()
    images = AnythingModel.objects.filter(directory__name=directory)

    return render(request, "app_anything/directory_detail.html", context={
        "season": season, 
        "dir": dir, 
        "images": images, 
    })
