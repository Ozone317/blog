from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm

# Create your views here.

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all_posts.html", {
#         "posts": all_posts
#     })

class AllPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


# def post_details(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
    
#     return render(request, "blog/post_details.html", {
#         "post": identified_post,
#         "tags": identified_post.tags.all()
#     })

class SinglePostView(DetailView):
    template_name = "blog/post_details.html"
    model = Post

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context