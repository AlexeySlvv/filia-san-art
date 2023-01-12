from django.urls import path
from . import views

urlpatterns = [
    path("", views.season_list, name="root-season-list"),
    path("anything/", views.season_list, name="season-list"),
    path("anything/<str:season>/", views.season_detail, name="season-detail"),
    path("anything/<str:season>/<str:directory>/", views.directory_detail, name="directory-detail"),
]
