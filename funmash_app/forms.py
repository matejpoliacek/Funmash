from django import forms
from funmash_app.models import UserProfile, Image
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# once we have 'upload image' functionality, this form
# will be required