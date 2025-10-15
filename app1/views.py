from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
def regist_fase2(request):
    if request.method=='POST':
        form=forms.Create_Team_Forem(request.POST)
        if form.is_valid():
            Team=form.save()
            login(request,Team)
            return redirect('Home')
        else:
            messages.error(request,'somthing wrong with your data call the orgnaizing Team')
        return render(request,'fas2.html',{'form':form})
    else:
        form=forms.Create_Team_Forem()
        return render(request,'fas2.html',{'form':form})
    

def home(request):
    return render(request,'Home.html')

@login_required
def submit(request):
    if request.method=='POST':
        form=forms.submit_form(request.POST)
        if form.is_valid():
            project_urls=form.save(commit=False)
            project_urls.Team=request.user
            project_urls.save()
            messages.success(request,'Project submitted successfully')
            return redirect('submitted_successfully')
        else:
            messages.error(request,'data is wrong call the organizing Team')
            return render (request,'submit.html',{'form':form})
    else:
        form =forms.submit_form()
        return render(request,'submit.html',{'form':form})
            
def successfully(request):
    return render (request,'successfully.html')


def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not  None:
            login(request,user)
            return redirect('Home')
        else :
            messages.error(request,'invaled Name or Password')
    return render(request,'Login.html')

def project_list(request):
    projects=models.project.objects.all()
    return render(request,'project_list.html',{'projects':projects})

    
        
            

    
    
    




    
