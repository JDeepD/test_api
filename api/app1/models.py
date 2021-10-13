from django.db import models

# Create your models here.

class Jokes(models.Model):
    content = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date']
