from django.db import models
from django.db.models import CharField


class Genre(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Creator(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)
    surname = models.CharField(max_length=32, null=False, blank=False)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['surname', 'name']

    def __repr__(self):
        return f"Creator(name={self.name}, surname={self.surname})"

    def __str__(self):
        return f"{self.name} {self.surname}"


class Movie(models.Model):
    title_orig = CharField(max_length=50, null=False, blank=False)
    title_cz = CharField(max_length=50, null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name='movies')
    directors = models.ManyToManyField(Creator, blank=True,
                                       related_name='directing')
    actors = models.ManyToManyField(Creator, blank=True, related_name='acting')
    length = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title_cz']

    def __repr__(self):
        return f"Movie(title_orig={self.title_orig}"

    def __str__(self):
        return f"{self.title_orig} ({self.year})"
