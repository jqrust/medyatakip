from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import edit
from django.contrib.auth import authenticate, login, logout, get_user
from .models import Survey

class LoginView(generic.View):
    template_name = 'main/login.html'
    def get(self,request,*args,**kwargs):
        return render(request,"main/login.html")
    def post(self,request,*args,**kwargs):
        username = request.POST['email']
        password = request.POST['password']    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            context = {
                "not_user": True
            }
            return render(request,"main/login.html", context)
        return render(request,"main/login.html")
def logout_view(request):
    logout(request)
    return redirect("../")
def home_view(request):
    return render(request,"main/home.html",{})

class SurveyCreate(edit.CreateView):
    model = Survey
    fields = ['name','ask_count','surveyors','fee']
