from django.shortcuts import render
import json

# Create your views here.


def artist_list(request):
    with open('Art.json', encoding='utf-8', mode='r') as json_file:
        data = json.load(json_file)
        artists = sorted(data.keys())
    return render(request, 'art/artist_list.html', context={
        'artists': artists,
    })


def artist_detail(request, artist):
    return render(request, 'art/artist_list.html', context={
        'artists': [artist],
    })
