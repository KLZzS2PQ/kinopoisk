from django.db.models import (
    Model, TextChoices, CharField, DateField, TextField,
    ImageField, FloatField, PositiveSmallIntegerField,
    ManyToManyField, PositiveIntegerField, ForeignKey, SET_NULL,
    CASCADE, DateTimeField
)

from apps.Core.models import User


# class MoviePersonRole(Model):
#        name = CharField(max_length=255)


class MoviePerson(Model):
    class RoleType(TextChoices):
        ACTOR = 'actor', 'Actor'
        DIRECTOR = 'director', 'Director'

    name = CharField(max_length=255)
    role = CharField(
        max_length=255, choices=RoleType.choices,
        blank=True, null=True
    )
    birth_date = DateField()
    photo = ImageField(upload_to='kinopoisk/images/person/photos/',
                       blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(Model):
    name = CharField(max_length=255)
    description = TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=255)
    description = TextField()
    release_date = DateField()
    rating = FloatField()
    duration = PositiveSmallIntegerField()
    genres = ManyToManyField(
        Genre, related_name='movies'
    )
    actors = ManyToManyField(
        MoviePerson, related_name='acted_in_movies'
    )
    directors = ManyToManyField(
        MoviePerson, related_name='directed_movies'
    )
    budget = PositiveIntegerField()
    poster = ImageField(
        upload_to='kinopoisk/images/movies/posters/',
        blank=True, null=True
    )


class MovieReview(Model):
    author = ForeignKey(User, on_delete=SET_NULL, null=True)
    movie = ForeignKey(Movie, on_delete=CASCADE)
    text = TextField()
    likes = PositiveIntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)
