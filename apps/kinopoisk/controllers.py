from django.shortcuts import render


def main(request):
    return render(request, 'kinopoisk/main.html')


def movie_list(request):
    return render(request, 'kinopoisk/movie_list.html')


def director_list(request):
    return render(request, 'kinopoisk/director_list.html')


def genre_list(request):
    return render(request, 'kinopoisk/genre_list.html')


def actors_list(request):
    return render(request, 'kinopoisk/actors_list.html')


def movie(request, id):
    return render(request)


def director(request, id):
    return render(request)


def genre(request, id):
    return render(request)


def actor(request, id):
    return render(request)
