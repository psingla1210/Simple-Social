from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()
###POSTS Models.py
# Create your models here.
class Post(models.Model):
     post_user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now=True)
     message = models.TextField()
     message_html = models.TextField(editable=False,default='', blank=True)
     group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

     def __str__(self):
         return self.message

     def save(self, *args, **kwargs):
         self.message_html = misaka.html(self.message)
         super().save(*args, **kwargs)

     def get_absolute_url(self):
         return reverse('posts:single', kwargs={'username':self.user.username,
                                                'pk':self.pk})

     class Meta:
         ordering = ['-created_at']
         unique_together = ['user','message']
