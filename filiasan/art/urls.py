from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='index'),
    path('art/', views.artist_list, name='artist_list'),
    path('art/<str:artist>/', views.artist_detail, name='artist-detail'),
]
