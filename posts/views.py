from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post #, Names
from django.contrib.auth.models import User
from .forms import SearchForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse  
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('home') 
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.names = Names.objects.get(user)  
        #     post.save()
        #     return redirect('home') 
    else: 
        form = PostForm()

    return render(request, 'upload.html', {'form': form})
def home(request):
    search_query = request.GET.get('search', '')  
    sort_by = request.GET.get('sort', '')
    posts = Post.objects.all().order_by('-created_at')  
    if search_query:
        posts = posts.filter(title__icontains=search_query)  
    if sort_by == 'most_liked':
        posts = posts.annotate(like_count=Count('likes')).order_by('-like_count', '-created_at')
    else:
        posts = posts.order_by('-created_at')
    context = {
        'posts': posts,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'home.html', context)

    # posts = Post.objects.all().order_by('-created_at') 

User = get_user_model()

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    liked = False
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user) 
    else:
        post.likes.add(user)  
        liked = True
    data = {
        'liked': liked,
        'total_likes': post.total_likes(),
    }
    return JsonResponse(data)
    #return redirect('post_detail', post_id=post_id)  
@login_required
def my_posts(request):
    user_posts = Post.objects.filter(author=request.user)  #change it to 'writer"
    return render(request, 'my_posts.html', {'posts': user_posts})
# Create your views here.
