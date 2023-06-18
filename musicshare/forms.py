from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Audio_store


class SignForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(label='Email / Username',required=True)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class AudioForm(forms.ModelForm):
    class Meta:
        model=Audio_store
        fields=('title','privacy','uploaded_for','music')

class CheckAudioForm(forms.ModelForm):
    class Meta:
        model=Audio_store
        fields=('title','privacy','uploaded_by','uploaded_for','music')
def clean_uploaded_by(self,email):
    data = self.cleaned_data['uploaded_by']
    data=email
    # do some stuff
    return data
