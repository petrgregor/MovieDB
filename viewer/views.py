from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView

from viewer.forms import GenreForm
from viewer.models import Movie, Creator, Genre


def home(request):
    movie = "Forrest Gump"
    released = 1994
    comments = ["Skvělý film.",
                "Velmi se mi to líbilo.",
                "Perfektní.",
                "Šlo to."]
    context = {'movie': movie, 'released': released, 'comments': comments}
    return render(request, 'viewer/home.html', context)


class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'viewer/genres.html'


class GenreDetailView(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'viewer/genre.html'


class GenreCreateView(CreateView):
    form_class = GenreForm
    template_name = 'viewer/form.html'
    success_url = reverse_lazy('genres')


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'viewer/form.html'
    success_url = reverse_lazy('genres')


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'viewer/confirm_delete.html'
    success_url = reverse_lazy('genres')


# Seznam filmů pomocí funkce
def movies(request):
    movies_list = Movie.objects.all()
    context = {'movies': movies_list}
    return render(request, 'viewer/movies.html', context)


# Seznam filmů pomocí třídy
class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'viewer/movies.html'


class CreatorListView(ListView):
    model = Creator
    context_object_name = 'creators'
    template_name = 'viewer/creators.html'


class CreatorDetailView(DetailView):
    model = Creator
    context_object_name = 'creator'
    template_name = 'viewer/creator.html'
