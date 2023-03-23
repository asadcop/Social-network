from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post_description=models.TextField()
    post_image=models.FileField(upload_to='core/post/', null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    numbers_of_likes=models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)
class Friend(models.Model):
    sender=models.ForeignKey(User, null=True,on_delete=models.CASCADE, related_name='fsender')
    receiver=models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='freceiver')
    is_friend=models.BooleanField(default=False)
    def __str__(self):
        return str(self.receiver)

class Like(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    liker=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.post)

class Notification(models.Model):
    resiver=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    is_seen=models.BooleanField(default=False)
    def __str__(self):
        return str(self.title)