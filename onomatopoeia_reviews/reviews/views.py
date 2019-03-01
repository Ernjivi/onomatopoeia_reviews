from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from reviews.models import Movie, Review, Vote
from reviews.forms import ReviewForm


def movie_list(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'movie-list.html', context)

@login_required
def movie_detail(request, movie_id):
    if request.method == 'GET':
        context = {
           'movie': get_object_or_404(Movie, pk=movie_id),
           'movie_form': ReviewForm()
        }
        # try:
        #     movie = Movie.objects.get(pk=movie_id)
        # except Movie.DoesNotExist:
        #     return Http404()
        return render(request, 'movie-detail.html', context)
    elif request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie_id = movie_id
            review.save()
            return HttpResponseRedirect(reverse('movie-detail', args=[movie_id]))
        else:
            context = {
                'movie': get_object_or_404(Movie, pk=movie_id),
                'movie_form': review_form
            } 
            return render(request, 'movie-detail.html', context)

@login_required
def add_vote(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.votes.create(user=request.user)
    return HttpResponseRedirect(reverse('movie-detail', args=[review.movie_id]))
