
from django import forms
from .models import Profile

from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'biografia']
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 4, 'maxlength': 500}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


from .models import Blog  

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'image']


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class CustomUserEditForm(UserChangeForm):
    password = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
        
