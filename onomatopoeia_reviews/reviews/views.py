from django.shortcuts import render
from reviews.models import Movie


def movie_list(request):
    print(request.method)
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'movie-list.html', context)


# for review in Review.objects.all():
#     print(review.content)