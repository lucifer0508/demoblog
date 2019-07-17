from django.db import models

# Create your models here.

class Contact(models.Model):
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=40, default='Empty...')
    comment = models.TextField()

    def __str__(self):
        return self.title