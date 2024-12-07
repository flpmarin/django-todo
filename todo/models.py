from django.db import models

# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    