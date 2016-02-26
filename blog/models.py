from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.title

def post_dir_path(instance, filename):
    return 'post/{0}/{1}_{2}'.format(instance.post.id, instance.id, filename)

class Section(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to=post_dir_path, default="")
    text = models.TextField()
    
    def __str__(self):
        return self.title

