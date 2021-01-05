from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name','content','colorText','colorBackground','fontSize']
        widgets = {
            'colorText':forms.TextInput(attrs={'type':'color'}),
            'colorBackground':forms.TextInput(attrs={'type':'color'})
        }
