from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [ 'username','email','password1', 'password2']
        widgets = {

            'username': forms.widgets.TextInput(attrs={
                'id': 'post-text', 
                'required': True, 
                'placeholder': 'User Name ',
                'class':'form-control'
            }),

            'email' : forms.widgets.EmailInput(attrs={
                'id': 'post-text', 
                'required': True, 
                'placeholder': 'Email Address',
                'class':'form-control'  
            }),

            'password1' : forms.widgets.PasswordInput(

                attrs={
                'placeholder': "password", 
                "class": "form-control"
                }),

            'password2' : forms.widgets.PasswordInput(attrs={
                'id': 'post-text', 
                'required': True, 
                'placeholder': '',
                'class':'form-control'  
            })
             
            
        
        
        
        }
