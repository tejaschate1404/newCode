# admin.py
from django.contrib import admin
from .models import Contact
from .models import webReview
from .models import Meeting


# Register the Contact model
admin.site.register(Contact)
admin.site.register(Meeting)
admin.site.register(webReview)
