from django.urls import path
from reviews import views

urlpatterns = [
    path('movie-list/', views.movie_list),
    path('movie-detail/<movie_id>/', views.movie_detail, name='movie-detail'),
]