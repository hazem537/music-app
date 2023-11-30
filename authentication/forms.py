from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class LoginForm (forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput)

    # def clean_username(self):
    #     username= self.cleaned_data["username"]
    #     if User.objects.filter(username = username).exists():
    #         return username 
    #     else:
    #         raise forms.ValidationError("this user name not exist")

    def clean_username(self):
        data = self.cleaned_data["username"]
        if User.objects.filter(username =data).exists():
            pass
        else:
            raise forms.ValidationError("this username not exist")
        
        return data
    
    def clean_password(self):
        username = self.data["username"]
        data = self.cleaned_data["password"]
        user = authenticate(username= username,password =data )
        if user is not None:
            pass
        else:
            raise forms.ValidationError("the  password is in correct") 
        return data
    

    def clean(self):
        user = user = authenticate(username= self.data["username"],password =self.data["password"])
        if user is not None:
            return user
        else:
            raise forms.ValidationError("the password or username is incorrect ")