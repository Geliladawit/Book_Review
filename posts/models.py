from django.db import models
from django.conf import settings

# class Names(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       
#     def __str__(self):
#         return self.user.username
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    # names = models.ForeignKey('posts.Names', on_delete=models.CASCADE, related_name='posts')  

    class Meta:
        ordering = ['-created_at']

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title
