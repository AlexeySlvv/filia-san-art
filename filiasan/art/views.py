from django.shortcuts import render
from .models import ArtistModel, ArtModel


def artist_list(request):
    artists = ArtistModel.objects.all().order_by("name")

    return render(request, 'art/artist_list.html', context={
        'artists': artists,
    })


def artist_detail(request, artist):
    works = ArtModel.objects.filter(artist__name=artist).order_by("year")

    return render(request, 'art/artist_detail.html', context={
        'artist': artist,
        'works': works,
    })
