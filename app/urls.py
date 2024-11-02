# bitbybyte/app/urls.py
from django.urls import path
from .views.home import HomeView
from .views.home import Review
from .views.home import demoBook
from .views.chatbot import ChatBotView
from .views.login import signup_view, login_view, logout_view
from .views.verify_email import *

urlpatterns = [
     path('', HomeView.as_view(), name='home'),
     path('review/', Review.as_view(), name='review'),
     path('demobook/', demoBook.as_view(), name='demobook'),
     path('chatbot/', ChatBotView.as_view(), name='chatbot'),
     path('signup/', signup_view, name='signup'),
     path('login/', login_view, name='login'),
     path('logout/', logout_view, name='logout'),
     path('verify1/', home ),
     path('verify2/', verify ),
]





    