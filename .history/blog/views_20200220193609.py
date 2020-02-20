from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown
import re

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
    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    post.text = md.convert(post.text)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', {"post": post})
