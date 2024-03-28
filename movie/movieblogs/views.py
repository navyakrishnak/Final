from django.http import HttpResponse
from django.shortcuts import render
from movielist.models import Movies
from django.contrib import messages,auth
from . models import MovieReview 
from django.contrib.auth.models import User



def index(request):
    try:
        username = request.session['username']
    except KeyError:
        username = "admin"
    
    # Fetch all movies from the database
    movies = Movies.objects.all()

    # Initialize empty lists for each category
   
    # Fetch only 3 movies for each category directly from the database
    thriller_movies = Movies.objects.filter(category__contains="thriller")[:3]
    action_movies = Movies.objects.filter(category__contains="action")[:3]
    comedy_movies = Movies.objects.filter(category__contains="comedy")[:3]

    return render(request, 'index.html', {
        'thriller_movies': thriller_movies, 
        'username': username, 
        'comedy_movies': comedy_movies,
        'action_movies': action_movies
    })

def action(request):
    action_movies = Movies.objects.filter(category__contains="action")
    return render(request,'actionmovies.html',{"action_movies":action_movies})

def comedy(request):
    comedy_movies = Movies.objects.filter(category__contains="comedy")
    return render(request,'comedymovies.html',{"comedy_movies":comedy_movies})

def thriller(request):
    thriller_movies = Movies.objects.filter(category__contains="thriller")
    return render(request,'thrillermovies.html',{"thriller_movies":thriller_movies})

def review(request,movie_name):
    print(movie_name)
    movie_names = movie_name
    print(movie_names)
    if request.method == 'POST':
        try:
            movie__name = movie_name
            username = request.session['username']
            rating = request.POST['rating']
            review = request.POST['review']
            rating = int(rating)
            if rating <= 10:


                reviews = MovieReview(username=username, movieName=movie__name, rating=rating, review=review)
                reviews.save()
                messages.success(request, "Your Review Successfully Submitted")
            else:
                messages.error(request,"Review Should Be UpTo 10")



        except KeyError:
            messages.error(request,"Error occured")

    return render(request,'review.html',{"moviename":movie_names})

def editmovie(request, movie_name):
    try:
        movie = Movies.objects.get(name=movie_name)
    except Movies.DoesNotExist:
        return HttpResponse("Movie does not exist")

    if request.method == 'POST':
        # Check if user is logged in
        if 'username' in request.session:
            username = request.session['username']
            try:
                # Update first name
                if 'movietitle' in request.POST:
                    movie.name = request.POST['movietitle']

                # Update description
                if 'desc' in request.POST:
                    movie.desc = request.POST['desc']

                # Update release date
                if 'rdate' in request.POST:
                    movie.releaseDate = request.POST['rdate']

                # Update actors
                if 'actors' in request.POST:
                    movie.actors = request.POST['actors']

                # Update poster
                if 'poster' in request.FILES:
                    movie.poster = request.FILES['poster']

                # Update YouTube link
                if 'youtubelink' in request.POST:
                    movie.youtubelink = request.POST['youtubelink']

                # Update category
                if 'category' in request.POST:
                    movie.category = request.POST['category']

                # Save the changes
                movie.save()
                messages.success(request, "Movie updated successfully")
            except Exception as e:
                messages.error(request, f"Error occurred: {str(e)}")
        else:
            messages.error(request, "You need to login to edit a movie")

    return render(request, 'editmovie.html', {"movie": movie})
