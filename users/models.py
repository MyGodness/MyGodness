from django.db import models
from django.contrib.auth.models import User

class MyGodnessUser(models.Model):
    GENDER_CHOICE = (
            ('M', 'Male'),
            ('F', 'Female'),
    )

    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    #email = models.EmailField()
    photo = models.ImageField(upload_to = 'static/img/', default="static/img/person_placeholder.png", null=True)
    motto = models.CharField(max_length=150)
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    major = models.CharField(max_length=30, null=False)
    school = models.CharField(max_length=50, null=False)



