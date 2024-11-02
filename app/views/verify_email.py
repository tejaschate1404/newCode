from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import *
from django.contrib.auth.models import User 
# from .models import Profile

import uuid


def home(request):
    if request.Method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_obj = User(username= email)
        user_obj.password (password)
        p_obj = Profile.objects.create(
            user = user_obj,
            email_token = str(uuid.uuid4())
        )
    

    return render(request, "app/email_verify.html")


def verify(request):
    try:
        obj = Profile.objects.get(email_token = token)
        obj.is_verified = True
        obj.save()
        return HttpResponse("is vefified successfully")
    except Exception as e :
        return HttpResponse("verified Pending")



