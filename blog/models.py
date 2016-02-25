from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=200, default="")
    text = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    commenter = models.CharField(max_length=100)

    def __str__(self):
        return self.comment_text
