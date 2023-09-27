from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from datetime import date
from .models import Post

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all_posts.html", {
        "posts": all_posts
    })

def post_details(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    
    return render(request, "blog/post_details.html", {
        "post": identified_post,
        "tags": identified_post.tags.all()
    })