from django.shortcuts import render, get_object_or_404
from reviews.models import Movie
from django.http import Http404


def movie_list(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'movie-list.html', context)

def movie_detail(request, movie_id):
    context = {
        'movie': get_object_or_404(Movie, pk=movie_id)
    }
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    # except Movie.DoesNotExist:
    #     return Http404()
    return render(request, 'movie-detail.html', context)

# for review in Review.objects.all():
#     print(review.content)