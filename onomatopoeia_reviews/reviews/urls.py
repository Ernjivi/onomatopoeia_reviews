from django.urls import path
from reviews import views

urlpatterns = [
    path('movie-list/', views.MyView.as_view(), name='movie-list'),
    path('movie-detail/<pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('create-review/<movie_id>/', views.ReviewCreate.as_view(), name="create-review"),
    path('add-vote/<review_id>/', views.add_vote, name='add-vote'),

]