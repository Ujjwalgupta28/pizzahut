from django.db import models

# Create your models here.
class USER(models.Model):

    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    user_Emailid=models.CharField(max_length=200)
    

