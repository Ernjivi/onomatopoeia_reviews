from rest_framework.routers import DefaultRouter
from reviews import views

router = DefaultRouter()
router.register('movies', views.MovieViewSet)

urlpatterns = router.urls

# from django.urls import path
# from reviews import views

# urlpatterns = [
#     path('movies/', views.movie_list, name='movie-list'),
#     path('movies/<pk>/', views.MovieDestroy.as_view()),
# ]