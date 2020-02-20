from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown

# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,
                  'blog/index.html',
                  context={
                      'title': '李虎的博客首页',
                      'post_list': post_list
                  })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.text = markdown.markdown(post.text,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', {"post": post})
