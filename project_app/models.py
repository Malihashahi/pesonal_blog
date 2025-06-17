from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=49)
    description = models.CharField(max_length=60)
    address = models.CharField(max_length=140)
    image = models.ImageField(upload_to="project")





    def __str__(self):
       return self.title