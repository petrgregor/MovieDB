"""
URL configuration for MovieDB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import *

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    path('genres/', GenreListView.as_view(), name='genres'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<int:pk>', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<int:pk>', GenreDeleteView.as_view(), name='genre_delete'),
    #path('movies/', movies, name='movies'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('creators/', CreatorListView.as_view(), name='creators'),
    path('creator/<int:pk>/', CreatorDetailView.as_view(), name='creator'),
]
