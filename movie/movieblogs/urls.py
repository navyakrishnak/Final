from django.urls import path
from . import views

app_name = 'movieblog'
urlpatterns = [
    path('',views.index, name="index"),
    path('action_movies',views.action, name="action"),
    path('comedy_movies',views.comedy, name="comedy"),
    path('thriller_movies',views.thriller, name="thriller"),
    path('review/<str:movie_name>/',views.review,name="review"),
    path('editmovie/<str:movie_name>/',views.editmovie,name="editmovie"),


]
