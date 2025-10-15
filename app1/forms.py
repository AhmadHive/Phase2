from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import project
class Create_Team_Forem(forms.ModelForm):
    confirm_password=forms.CharField()
    class Meta:
        model=User
        fields=['Team_name','password']
    def clean(self):
        clened_data=super().clean()
        password=clened_data.get('password')
        confirm=clened_data.get('confirm_password')
        if confirm !=password:
            raise forms.ValidationError('passwords don\' match')
        return clened_data
    def save(self, commit =True):
        username=self.cleaned_data['Team_name']
        Team_name=self.cleaned_data['Team_name']
        password=self.cleaned_data['password']
        user=User.objects.create_user(username=username,Team_name=Team_name,password=password)
        if commit :
            user.save()
        return user
    

class submit_form(forms.ModelForm):
    class Meta:
        model= project
        fields=['project_url']


            
            
    
    

