from django.test import TestCase

from viewer.forms import CreatorForm


class CreatorTestForm(TestCase):
    def test_creator_form_is_valid(self):
        creator_form = CreatorForm(
            data={
                'name': 'martin',
                'surname': 'Novák',
                'date_of_birth': '1975-09-15',
                'date_of_death': '2016-05-09',
                'biography': 'Biografie.'
            }
        )
        self.assertTrue(creator_form.is_valid())
