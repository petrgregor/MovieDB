from django.forms import ModelForm

from viewer.models import Genre, Creator, Movie


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class CreatorForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
