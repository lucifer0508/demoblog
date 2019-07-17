from django.db import models

# Create your models here.

class Blogdata(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    email = models.CharField(max_length=40, default='Empty...')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title