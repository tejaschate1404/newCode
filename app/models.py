
from django.db import models
from django.contrib.auth.models import User   


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.user
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    service = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class webReview(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Choices from 1 to 5

    def __str__(self):
        return f'{self.name} - {self.rating} Stars'
    


class Meeting(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"


