from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from reviews.models import Movie, Review, Vote
from reviews.forms import ReviewForm

from django.views.generic import ListView, DetailView, CreateView


class MyView(ListView):
    model = Movie
    template_name = 'movie-list.html'

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie-detail.html'

@method_decorator(login_required, name='dispatch')
class ReviewCreate(CreateView):
    model = Review
    fields = ['content']
    
    def post(self, request, *args, **kwargs):
        self.object = None
        self.movie_id = kwargs['movie_id']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.movie_id = self.movie_id
        self.object.save()
        return HttpResponseRedirect(reverse('movie-detail', args=[self.movie_id]))




@login_required
def add_vote(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.votes.create(user=request.user)
    return HttpResponseRedirect(reverse('movie-detail', args=[review.movie_id]))
