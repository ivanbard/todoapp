from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #if user deleted, delete(cascade) their tasks with them
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) #automatically take the time and date at creation

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete'] #order by the complete values above