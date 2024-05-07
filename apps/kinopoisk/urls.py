from django.urls import path

from apps.kinopoisk.controllers import (
    movie_list, director_list, genre_list, actor_list, main,
    movie_detail, genre_detail, person_detail, add_review, add_review_like,
)

urlpatterns = [
    path('', main, name='main'),

    path('movies/', movie_list, name='movie_list'),
    path('actors/', actor_list, name='actors_list'),
    path('directors/', director_list, name='director_list'),
    path('genres/', genre_list, name='genre_list'),

    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('person/<int:person_id>/', person_detail, name='person_detail'),
    path('genre/<int:genre_id>/', genre_detail, name='genre_detail'),

    path('review/', add_review, name='add_review'),
    path('add_review_like/', add_review_like, name='add_review_like'),
]
