from django.db import models

# Create your models here.

class Footer(models.Model):
   address = models.CharField(max_length=100)
   city = models.CharField(max_length=40)
   phone = models.CharField(max_length=50)
   email = models.EmailField()


   whatsapp= models.CharField(max_length=100)
   telegram = models.CharField(max_length=100)
   instagram = models.CharField(max_length=100)


class Massage(models.Model):
   fname = models.CharField(max_length=50)
   email = models.EmailField()
   sub = models.CharField(max_length=100)
   body = models.TextField()


   def __str__(self) :
       return f"{ self.fname} + {self.email}"