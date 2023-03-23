import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Messages(models.Model):
    sender=models.ForeignKey(User, null=True,on_delete=models.CASCADE, related_name='sender')
    receiver=models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='receiver')
    message=models.TextField()
    sendtime=models.DateTimeField(default=datetime.datetime.now,blank=None, null=None)
    is_seen=models.BooleanField(default=False)
    def __str__(self):
        return str(self.sender)