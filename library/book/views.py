from django.shortcuts import render, redirect
from book.forms import CommentForm, BlogPostForm, AuthorForm


def home(request):
    data = {"comment_form": BlogPostForm()}
    return render(request, "my_form.html", data)

################################################################################

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

####################################################################

def author(request):
    data = {"author_form": AuthorForm()}
    return render(request, "my_form.html", data)


def author_form(request):
    data = {"author_form": AuthorForm()}
    return render(request, "author_form.html", data)


def new_author(request):
    if request.method == "POST":
        form = author_form(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/my_form_view")

    else:
        form = author_form()
    data = {'form': form}
    return render(request,"author/new_author.html", data)

########################################################################

def my_form_view(request):
    data = {"comment_form": CommentForm()}
    return render(request, "my_form.html", data)


def comment_form(request):
    data = {"comment_form": CommentForm()}
    return render(request, "comment_form.html", data)


def new_comment(request):
    if request.method == "POST":
        form = comment_form(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/my_form_view")

    else:
        form = comment_form()
    data = {'form': form}
    return render(request,"comment/new_comment.html", data)