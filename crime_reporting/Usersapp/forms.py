from django import forms
from .models import Complaint,feedback,Profile,plogin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ['username',  'password']

class policeForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)

    class Meta:
        model = plogin
        fields = ['username',  'password']


class UserComplaintForm(forms.ModelForm):
    username = forms.CharField(required=False)
    mobile = forms.IntegerField(required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":15}),required=False)
    city = forms.CharField(required=False)
    complaint_title = forms.CharField(required=False)
    complaint_details = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":15}),required=False)

    class Meta:
        model = Complaint
        fields = '__all__'


class UserFeedbackForm(forms.ModelForm):
    username = forms.CharField(required=False)
    mobile = forms.IntegerField(required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":15}),required=False)
    city = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    feedback = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":15}),required=False)

    class Meta:
        model = feedback
        fields ='__all__'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
  
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']  
    
    

    



