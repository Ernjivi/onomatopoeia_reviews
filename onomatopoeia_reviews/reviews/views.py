from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from reviews.models import Movie, Review, Vote
from reviews.forms import ReviewForm

from django.views.generic import ListView, DetailView, CreateView, View


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.generics import DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from reviews.serializers import MovieSerializer


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


# @api_view(['get', 'post'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie_list = Movie.objects.all()
#         serializer = MovieSerializer(movie_list, many=True)
#         return Response(serializer.data)
#     else:
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# class MovieDestroy(DestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# api/recursos/ GET POST
# api/recursos/id/ GET PUT PATCH DELETE
# api/recursos/id/add-vote/ 

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer