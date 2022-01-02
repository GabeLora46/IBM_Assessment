from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Used for registering user
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'password1', 'password2']

#Used for Updating users
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username', 'email',]

#Used when users what to update their profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'img']