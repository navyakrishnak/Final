from django.urls import path
from . import views

app_name = 'movielist'
urlpatterns = [
    path('',views.addmovie, name="addmovie"),
    

    
]
