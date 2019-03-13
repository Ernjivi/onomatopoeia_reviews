from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from reviews.models import Movie, Review, Vote
from reviews.forms import ReviewForm

from django.views.generic import ListView, DetailView, CreateView, View


# from rest_framework.decorators import api_view
# from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status

from reviews.serializers import MovieSerializer, ReviewSerializer


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


@method_decorator(login_required, name='dispatch')
class AddVote(View):
    def get(self, request, *args, **kwargs):
        review_id = kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        review.votes.create(user=self.request.user)
        return HttpResponseRedirect(reverse('movie-detail', args=[review.movie_id]))
        

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @action(detail=True, methods=['get'], url_path='add-vote')
    def add_vote(self, request, pk=None):
        review = self.get_object()
        review.votes.create(user=request.user)
        return Response({}, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['delete'], url_path='delete-vote')
    def delete_vote(self, request, pk=None):
        review = self.get_object()
        review.votes.filter(user=request.user).delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
