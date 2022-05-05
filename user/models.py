from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField("First Name", max_length=255)
    lastname = models.CharField("Last Name", max_length=255)
    dob = models.DateTimeField(auto_now_add=True)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=2, null=False, choices=gender_choices)