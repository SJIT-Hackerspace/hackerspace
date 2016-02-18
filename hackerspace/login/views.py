from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
import re

# Create your views here.
def login(request):
    return render(request,"login/index.html")
def validate(request):
    form_details = request.POST
    user = authenticate(username=form_details['username'],password=form_details['password']);
    if user is not None:
        if user.is_active:
            return render(request,'/feed/')
    else:
        return HttpResponse("You are not registered.")

def register(request):
    registration_details = request.POST
    if( registration_details['password'] == registration_details['rpassword'] ):
        user = User.objects.create_user(registration_details['username'],registration_details['password'])
        user.save();
