from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.kinopoisk.models import Movie, Genre, MoviePerson, MovieReview, UserMovieReviewVote


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
        'movie': Movie.objects.get(id=movie_id),
        'reviews': MovieReview.objects.filter(
            movie_id=movie_id,
        ).order_by('-created_at')
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


@api_view(('POST',))
def add_review(request):
    if not request.user.is_authenticated:
        return Response(status=403, data={'success': False})
    movie_id = int(request.data['movie_id'])
    review = MovieReview.objects.create(
        author=request.user,
        text=request.data['review'],
        movie_id=movie_id
    )
    return Response({
        'author_name': review.author.username,
        'text': review.text,
        'created_at': review.created_at,
    })


@api_view(('POST',))
def add_review_like(request):
    if not request.user.is_authenticated:
        return Response(status=403, data={'success': False})
    review_id = request.data['review_id']
    try:
        review = UserMovieReviewVote.objects.get(
            user=request.user,
            review_id=review_id
        )
        review.delete()
        return Response(status=200, data={
            'success': True,
            'vote': False
        })
    except UserMovieReviewVote.DoesNotExist:
        UserMovieReviewVote.objects.create(
            user=request.user,
            review_id=review_id
        )
        return Response(status=200, data={
            'success': True,
            'vote': True
        })
