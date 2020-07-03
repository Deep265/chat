from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse

# Create your models here.
class SMS(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('messages:users',kwargs={'username':self.user.username,'pk':self.pk})