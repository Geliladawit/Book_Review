from django.contrib import admin
from .models import Post#, Names

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'total_likes')
        # list_display = ('title', 'names', 'created_at', 'total_likes')


admin.site.register(Post)
