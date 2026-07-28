from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1']
