from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField(max_length=1000) 


    def __str__(self):
        return self.title # to put the title on the home app in the admin site