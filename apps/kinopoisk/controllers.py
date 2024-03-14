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
        )
    })


def actor_list(request):
    return render(request, 'kinopoisk/person_list.html', {
        'persons': MoviePerson.objects.filter(
            role=MoviePerson.RoleType.ACTOR
        )
    })


def genre_list(request):
    return render(request, 'kinopoisk/genre_list.html', {
        'genres': Genre.objects.all()
    })


def movie_detail(request, id):
    return render(request, 'kinopoisk/movie_detail.html', {
        'movie': Movie.objects.get(id=id)
    })


def director_detail(request, id):
    director = MoviePerson.objects.get(id=id)
    return render(request, 'kinopoisk/person_detail.html', {
        'person': director,
        'movies': director.directed_movies.all()
    })


def actor_detail(request, id):
    actor = MoviePerson.objects.get(id=id)
    return render(request, 'kinopoisk/person_detail.html', {
        'person': actor,
        'movies': actor.acted_in_movies.all()
    })


def genre_detail(request, id):
    genre = Genre.objects.get(id=id)
    return render(request, 'kinopoisk/genre_detail.html', {
        'genre': genre,
        'movies': genre.movies.all()
    })
