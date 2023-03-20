from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Massages(models.Model):
    sender=models.ForeignKey(User, null=True,on_delete=models.CASCADE, related_name='sender')
    receiver=models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='receiver')
    massage=models.TextField()
    sendtime=models.DateTimeField()
    is_seen=models.BooleanField(default=False)
    def __str__(self):
        return self.sender