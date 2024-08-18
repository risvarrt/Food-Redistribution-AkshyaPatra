from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        
        
class UserRegisterForm1(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['type_of_user', 'premium_accout','image']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email',]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['type_of_user','premium_accout','image',]

class ProfileUpdateForm1(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nature_of_institution','name_of_institution','your_role','mobile_no','address','city','pincode','any_thing_would_you_like_to_tell_us']

class ProfileUpdateForm2(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name_of_institution','mobile_no','address','city','pincode','latitude','longitude','does_it_have_kitchen','does_it_accept_raw_food','please_specify_food_perference','status_of_registration','any_thing_would_you_like_to_tell_us']

class ProfileUpdateForm3(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['how_would_you_like_to_help','mobile_no','address','city','pincode','any_thing_would_you_like_to_tell_us']