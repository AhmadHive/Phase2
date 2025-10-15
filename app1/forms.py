from django import forms
from django.contrib.auth.models import User
from .models import project

class Create_Team_Form(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )
    
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': 'Team Name (Username)',
            'password': 'Password'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')
        
        if password and confirm and password != confirm:
            raise forms.ValidationError('كلمات المرور غير متطابقة')
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class submit_form(forms.ModelForm):
    class Meta:
        model = project
        fields = ['project_url']
        labels = {
            'project_url': 'Project URL'
        }
        help_texts = {
            'project_url': 'Enter the URL of your project (GitHub, Live Demo, etc.)'
        }