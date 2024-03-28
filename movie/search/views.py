from django.shortcuts import render

from movielist.models import Movies
from django.db.models import Q

# Create your views here.
def search(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movies.objects.all().filter(Q(name__contains =query) | Q(desc__contains = query))
        print(movies)
    return render(request, 'search.html',{'query':query, 'movie':movies})