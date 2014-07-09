from django.shortcuts import render_to_response, render, redirect
from Hollywood.forms import GenreForm, MovieForm, ActorForm
from Hollywood.models import Genre, Movie, Actor


def home(request):
    return render(request, "home.html")


def genres(request):
    genres = Genre.objects.all()
    return render_to_response("genre/genre.html", {'genres': genres})


def new_genre(request):
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        form = GenreForm(request.POST)

        # Django will check the form's validity for you
        if form.is_valid():

            # Saving the form will create a new Genre object
            if form.save():

                # After saving, redirect the user back to the index page
                return redirect("/genres")

    # Else if the user is looking at the form page
    else:
        form = GenreForm()
    data = {'form': form}
    return render(request, "genre/new_genre.html", data)


def view_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    data = {"genre": genre}
    return render(request, "genre/view_genre.html", data)


def edit_genre(request, genre_id):
    # Similar to the the detail view, we have to find the existing genre we are editing
    genre = Genre.objects.get(id=genre_id)

    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            if form.save():
                return redirect("/genres/{}".format(genre_id))

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = GenreForm(instance=genre)
    data = {"genre": genre, "form": form}
    return render(request, "genre/edit_genre.html", data)


def delete_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    genre.delete()
    return redirect("/genres")


##################################movies############

# def movies(request):
#     return render_to_response("movies.html")

def movies(request):
    movies = Movie.objects.all()
    return render_to_response("Movies/movies.html", {'movies': movies})


def new_movie(request):
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        form = MovieForm(request.POST)

        # Django will check the form's validity for you
        if form.is_valid():

            # Saving the form will create a new Movie object
            if form.save():

                # After saving, redirect the user back to the index page
                return redirect("/movies")

    # Else if the user is looking at the form page
    else:
        form = MovieForm()
    data = {'form': form}
    return render(request, "Movies/new_movie.html", data)


def view_movies(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    data = {"movie": movie}
    return render(request, "Movies/view_movies.html", data)


def edit_movie(request, movie_id):
    # Similar to the the detail view, we have to find the existing genre we are editing
    movie = Movie.objects.get(id=movie_id)

    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            if form.save():
                return redirect("/movies/{}".format(movie_id))

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = GenreForm(instance=genre)
    data = {"movie": movies, "form": form}
    return render(request, "movies/edit_movie.html", data)


def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect("/movie")


###################actor##################################################################

def actor(request):
    actors = Actor.objects.all()
    return render_to_response("Actor/actors.html", {'actors': actors})


def new_actor(request):
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        form = ActorForm(request.POST)

        # Django will check the form's validity for you
        if form.is_valid():

            # Saving the form will create a new Genre object
            if form.save():

                # After saving, redirect the user back to the index page
                return redirect("/actors/")

    # Else if the user is looking at the form page
    else:
        form = ActorForm()
    data = {'form': form}
    return render(request, "Actor/new_actor.html", data)


def view_actors(request, actor_id):
    actor = Actor.objects.get(id=actor_id)
    data = {"actors": actor}
    return render(request, "Actor/view_actor.html", data)
