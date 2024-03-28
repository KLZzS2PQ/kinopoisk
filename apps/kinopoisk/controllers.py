from django.shortcuts import render

from apps.kinopoisk.models import Movie, Genre, MoviePerson


def main(request):
    return render(request, 'kinopoisk/main.html')


def movie_list(request):
    return render(request, 'kinopoisk/movie_list.html', {
        'movies': Movie.objects.all()
    })


def director_list(request):
    return render(request, 'kinopoisk/person_list.html', {
        'persons': MoviePerson.objects.filter(
            role=MoviePerson.RoleType.DIRECTOR
        ),
        'role': MoviePerson.RoleType.DIRECTOR
    })


def actor_list(request):
    return render(request, 'kinopoisk/person_list.html', {
        'persons': MoviePerson.objects.filter(
            role=MoviePerson.RoleType.ACTOR
        ),
        'role': MoviePerson.RoleType.ACTOR
    })


def genre_list(request):
    return render(request, 'kinopoisk/genre_list.html', {
        'genres': Genre.objects.all()
    })


def movie_detail(request, movie_id):
    return render(request, 'kinopoisk/movie_detail.html', {
        'movie': Movie.objects.get(id=movie_id)
    })


def person_detail(request, person_id):
    person = MoviePerson.objects.get(id=person_id)
    if person.role == MoviePerson.RoleType.ACTOR:
        movies = person.acted_in_movies.all()
    else:
        movies = person.directed_movies.all()
    return render(request, 'kinopoisk/person_detail.html', {
        'person': person,
        'movies': movies
    })


def genre_detail(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    return render(request, 'kinopoisk/genre_detail.html', {
        'genre': genre,
        'movies': genre.movies.all()
    })
