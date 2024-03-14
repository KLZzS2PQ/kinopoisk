from django.contrib import admin

from apps.Core.models import User
from apps.kinopoisk.models import MoviePerson, Genre, Movie, MovieReview


@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'birth_date', 'photo',)
    list_editable = ('role', 'photo',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    list_editable = ('name', 'description',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'release_date', 'rating', 'duration', 'budget',
        'poster'
    )
    list_editable = (
        'release_date', 'rating', 'duration', 'budget', 'poster'
    )


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'movie',)
