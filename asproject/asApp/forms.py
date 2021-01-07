from django import forms
from django.contrib.auth.models import User
from asApp.models import Request,Update
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# create your form here.
class CustomerCreationForm(UserCreationForm):
    username = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='First_Name')
    last_name = forms.CharField(required=True, label='Last_Name')

    class Meta:
        model = User
        fields = ['username','first_name','last_name']

class CustomerLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = '__all__'
