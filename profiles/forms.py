from django import forms
from .models import Profile


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'avatar')
