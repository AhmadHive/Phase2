from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models

def regist_fase2(request):
    if request.method == 'POST':
        form = forms.Create_Team_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Team account created successfully!')
            return redirect('Home')
        else:
            messages.error(request, 'Something wrong with your data, please contact the organizing team')
    else:
        form = forms.Create_Team_Form()
    
    return render(request, 'fas2.html', {'form': form})

def home(request):
    return render(request, 'Home.html')

@login_required
def submit(request):
    if request.method == 'POST':
        form = forms.submit_form(request.POST)
        if form.is_valid():
            project_obj = form.save(commit=False)
            project_obj.Team = request.user
            project_obj.save()
            messages.success(request, 'Project submitted successfully!')
            return redirect('submitted_successfully')
        else:
            messages.error(request, 'Invalid data, please check your project URL')
    else:
        form = forms.submit_form()
    
    return render(request, 'submit.html', {'form': form})

def successfully(request):
    return render(request, 'successfully.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('Home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'Login.html')

def project_list(request):
    projects = models.project.objects.all().order_by('-Submitted_at')
    return render(request, 'project_list.html', {'projects': projects})