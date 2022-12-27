from django.db import models

# Create your models here.
class Entry(models.Model):
    G = (
        ("M", "Male"),("F", "Female"),("O", "Other")
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_img = models.ImageField(null=True,default="")
    email = models.EmailField(max_length=300)
    contact = models.FloatField(max_length=50)
    gender = models.CharField(max_length=20,)
    day = models.IntegerField(blank=True,null=True)
    month = models.CharField(max_length=20,blank=True,null=True)
    year = models.IntegerField(blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True )
    country = models.CharField(max_length=50,blank=True,null=True)
    documents = models.FileField(upload_to="news/", max_length=250, null=True, default=None)
    passwords = models.CharField(max_length=50, default="")
