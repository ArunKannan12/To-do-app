from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter user name','style':'width:400px;height:50px;border-radius:10px;border:2px #dc3545 solid;'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'enter E-mail','style':'width:400px;height:50px;border-radius:10px;border:2px #dc3545 solid;'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'enter password','style':'width:400px;height:50px;border-radius:10px;border:2px #dc3545 solid;'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-enter password','style':'width:400px;height:50px;border-radius:10px;border:2px #dc3545 solid;'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email

class TaskForm(forms.ModelForm):
    
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter user name','style':'height:30px;'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'enter description'}))
    class Meta:
        model = Task
        fields = ['title','description','complete']
