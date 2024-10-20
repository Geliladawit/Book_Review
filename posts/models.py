from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
  
    class Meta:
        ordering = ['-created_at']

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title
