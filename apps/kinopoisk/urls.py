from django.urls import path

from apps.kinopoisk.controllers import (
    movie_list, director_list, genre_list, actor_list, main,
    movie_detail, director_detail, genre_detail, actor_detail
)

urlpatterns = [
    path('', main, name='main'),

    path('movies/', movie_list, name='movies'),
    path('directors/', director_list, name='director_list'),
    path('genres/', genre_list, name='genre_list'),
    path('actors/', actor_list, name='actors_list'),

    path('movie/<int:id>/', movie_detail, name='movie_detail'),
    path('director/<int:id>/', director_detail, name='director_detail'),
    path('genre/<int:id>/', genre_detail, name='genre_detail'),
    path('actor/<int:id>/', actor_detail, name='actor_detail'),
]
