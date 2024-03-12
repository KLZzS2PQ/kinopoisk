from django.urls import path

from apps.kinopoisk.controllers import (
    movie_list, movie, director, genre, actor,
    director_list, genre_list, actors_list, main
)

urlpatterns = [
    path('', main, name='main'),

    path('movies/', movie_list, name='movies'),
    path('directors/', director_list, name='director_list'),
    path('genres/', genre_list, name='genre_list'),
    path('actors/', actors_list, name='actors_list'),

    path('movie/<int:id>/', movie, name='movie'),
    path('director/<int:id>/', director, name='director'),
    path('genre/<int:id>/', genre, name='genre'),
    path('actor/<int:id>/', actor, name='actor'),
]
