from django.shortcuts import render


def home(request):
    movie = "Forrest Gump"
    released = 1994
    comments = ["Skvělý film.",
                "Velmi se mi to líbilo.",
                "Perfektní.",
                "Šlo to."]
    context = {'movie': movie, 'released': released, 'comments': comments}
    return render(request, 'viewer/home.html', context)
