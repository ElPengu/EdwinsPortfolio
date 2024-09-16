from django.db import models

# Create your models here.

#To do list that references user
class todoListItem(models.Model):
    id = models.AutoField(primary_key=True) # Serial <-> AutoField
    user_id = models.ForeignKey('mainsite.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(auto_now_add=True) # made automatically
    dateCompleted = models.DateTimeField(null=True, blank=True)
