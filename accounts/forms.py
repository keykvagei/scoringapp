from django import forms
from django.contrib.auth.forms import UserCreationForm
from profiles.models import Profile



class NewUserForm(UserCreationForm):
	class Meta:
		model = Profile
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user