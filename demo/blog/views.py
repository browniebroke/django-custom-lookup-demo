from django.views.generic import ListView

from .models import Post


class BlogIndexView(ListView):
    template_name = "blog_index.html"
    context_object_name = "posts_list"
    queryset = Post.objects.filter(published_at__past=True).order_by("-published_at")
