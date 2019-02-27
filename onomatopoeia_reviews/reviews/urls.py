from django.urls import path
from reviews import views

urlpatterns = [
    path('movie-list/', views.movie_list)
]