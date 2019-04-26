from django import forms
from .models import Signup



class FormName(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'


from django import forms
from mainapp.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')

