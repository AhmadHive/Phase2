from django.urls import path
from . import views

urlpatterns=[
    path('regist',views.regist_fase2,name='regist'),
    path('Home',views.home,name='Home'),
    path('submit',views.submit,name='submit'),
    path('submitted_successfully',views.successfully,name='submitted_successfully'),
    path('Login',views.Login,name='Login'),
    path('list',views.project_list,name='project_list')
]