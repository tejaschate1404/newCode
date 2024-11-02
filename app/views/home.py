from django.views import View
from django.http import HttpResponse
from ..models import Contact
from ..models import webReview
from ..models import Meeting
from django.shortcuts import render

  
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'greeting': 'Hello, welcome to BitByByte!'
        }
        return render(request, 'app/home.html', context)
    
    def post(self, request):
        # Handle the POST request
        name = request.POST.get('name')  # Change 'name1' to 'name' to match your form field
        number = request.POST.get('number')
        service = request.POST.get('service')

        # Save to the database
        Contact.objects.create(name=name, number=number, service=service)

        return HttpResponse("Thank you for your submission!") 
    

class Review(View):
    def get(self, request, *args, **kwargs):
        reviews = webReview.objects.all()
        context = {
            'reviews': reviews
        }
        return render(request, 'app/review.html', context)    



 
    def post(self, request):
        # Get data from the POST request
        name = request.POST.get('name')
        review_text = request.POST.get('review')
        rating = request.POST.get('rating')

        # Save the review to the database
        name = webReview(name=name, review=review_text, rating=rating)
        name.save()

        return HttpResponse("Thank you for your review!")  # Response message after submission
    



class demoBook(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/demoBook.html')

    def post(self, request):
        # Get data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Save the meeting details to the database
        meeting = Meeting(name=name, email=email, message=message, date=date, time=time)
        meeting.save()

        return HttpResponse("Thank you for scheduling the meeting!") 




 