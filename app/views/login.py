# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.db import models





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=200)
    email_verify = models.BooleanField(default=False)

    def __str__(self):
        return self.user

# Signup View
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        
        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return redirect('login')
    return render(request, 'app/signup.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page after login
        else:
            return HttpResponse("Invalid login credentials")
    
    return render(request, 'app/login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')
