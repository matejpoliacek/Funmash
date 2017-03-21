from django import forms
from funmash_app.models import UserProfile, Image
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class FeedbackForm(forms.Form):
		# name = forms.CharField(max_length=128, help_text="username", required = True)
		# email = forms.CharField(max_length=128, help_text="email@email.email", required = True)
		# comments = forms.CharField(help_text="Feedback message default", required = True, widget=forms.Textarea)

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
		self.fields['content'].label = "What do you want to say?"