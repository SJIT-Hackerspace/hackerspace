from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request,"login/index.html")
def validate(request):
    form_details = request.POST
    user = authenticate(form_details['username'],form_details['password']);
    if user is not None:
        if user.is_active:
            return render(request,'/feed/')
