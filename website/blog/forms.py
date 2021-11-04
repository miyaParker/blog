from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreatePostForm(forms.Form):
    author = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Author Name'}), max_length=50, label="")
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Title'}), max_length=50, label="")
    category = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Category'}), max_length=50, label="")
    content = forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Content'}), label="")


class SignupForm(UserCreationForm):
    fullname = forms.CharField(max_length= 60, label="Full name")
    class meta:
        model = User


    
