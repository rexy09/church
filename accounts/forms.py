from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# User ragistration form
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill form-control', 'placeholder':'Username'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill form-control', 'placeholder':'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'rounded-pill form-control', 'placeholder':'Password',}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'rounded-pill form-control', 'placeholder':'Confirm password',}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'first_name',
            'last_name',
			'username',
			'email',
			'password1',
			'password2',
		]


# User login form
class LoginForm(forms.Form):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))


# Edit user form
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill form-control', 'placeholder':'Username'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'rounded-pill form-control', 'placeholder':'Email'}))
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]