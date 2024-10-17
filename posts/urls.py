from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Post 
from django.contrib import admin
from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('', views.home, name='home'),
    path('myposts/', views.my_posts, name='my_posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)