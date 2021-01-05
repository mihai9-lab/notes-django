from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
# Create your models here.


class Note(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    colorText = models.CharField(max_length=7, default='#333333')
    colorBackground = models.CharField(max_length=7, default='#ffffff')
    fontSize = models.PositiveIntegerField(default=16, validators=[
        MaxValueValidator(30, 'Font size has to be less than or equal to 30'),
        MinValueValidator(5, 'Font size has to be bigger than or equal to 5')
    ])
    completed = models.BooleanField(default=False)
    userId = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def is_completed(self):
        return self.completed
