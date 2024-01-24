from django.db import models

# Create your models here.

class Scholoarship(models.Model):

    name = models.CharField(max_length=200);
    majors = models.CharField(max_length=200);
    gpa = models.DOUBLE(max_length=4);
    discription = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name, self.majors, self.gpa, self.discription

