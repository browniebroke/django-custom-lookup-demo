from django.views.generic import ListView
from django.utils import timezone
from .models import Post


class BlogIndexView(ListView):
    template_name = 'blog_index.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(published_at__lt=timezone.now()).order_by('-published_at')
