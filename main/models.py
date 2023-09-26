from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import pytz


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now().astimezone(pytz.timezone('Africa/Nairobi')))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
