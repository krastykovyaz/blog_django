from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # posts has just one author
from django.urls import reverse # get absolut url string

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # related table by key for a user & user can delete the post as well 
    # CASCADE ia all upper case

    def __str__(self):
        return self.title

    #find the location of specific post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})