from django.shortcuts import render
from . models import Movies
from django.contrib import messages

# Create your views here.
def addmovie(request):
    try:
        username = request.session['username']  
        if request.method == "POST":
            name = request.POST['movietitle']
            poster = request.FILES['poster']
            desc = request.POST['desc']
            releaseDate = request.POST['rdate']
            youtubelink = request.POST['youtubelink']
            actors = request.POST['actors']
            category = request.POST.getlist('category')
            if username:
                movie = Movies.objects.create(name=name, poster=poster, desc=desc, releaseDate=releaseDate, youtubelink=youtubelink, username=username,  actors=actors, category=category)
                movie.save()
                messages.success(request, "Sucessfully added")
    except:
        messages.error(request,"Error occured")

           
    return render(request, 'addmovie.html')