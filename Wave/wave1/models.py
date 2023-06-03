from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')
    body = models.TextField()
    image = models.ImageField(upload_to='post_file', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
     
    def __str__(self):
        return self.title