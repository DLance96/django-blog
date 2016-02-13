from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField()

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
