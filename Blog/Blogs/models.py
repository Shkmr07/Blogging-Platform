from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    createAt = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    description = models.TextField()
    post = models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)

    def __str__(self):
        return self.description


