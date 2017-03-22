from django import forms
from funmash_app.models import UserProfile, Image
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class FeedbackForm(forms.Form):

	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
	
	def __init__(self, *args, **kwargs):
		super(FeedbackForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Your name:"
		self.fields['contact_email'].label = "Your email:"
		self.fields['content'].label = "Tell us what you think:"