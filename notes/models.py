from django.db import models

# Create your models here.

class Note(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)