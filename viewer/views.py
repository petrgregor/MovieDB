from django.shortcuts import render
from django.views.generic import ListView, DetailView

from viewer.models import Movie, Creator


def home(request):
    movie = "Forrest Gump"
    released = 1994
    comments = ["Skvělý film.",
                "Velmi se mi to líbilo.",
                "Perfektní.",
                "Šlo to."]
    context = {'movie': movie, 'released': released, 'comments': comments}
    return render(request, 'viewer/home.html', context)


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
