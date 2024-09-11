from django.db import models

# Create your models here.
#Arbitrary model
class Student(models.Model):
    #Can make queries in this way, 
    #but I am using SQL directly so that
    #I may gain practise.
    #Find in views
    name=models.CharField()
    desc=models.TextField()
    def __str__(self):
        return self.name

