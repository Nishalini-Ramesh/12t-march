from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def __str__(self):
    return self.username
