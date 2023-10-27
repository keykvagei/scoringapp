from django.shortcuts import render
from django.core.paginator import Paginator
from posts.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def feed_view(request):
    all_posts = Post.objects.order_by('-created_at')
    paginator = Paginator(all_posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'feed/feed.html', {'posts': posts})
