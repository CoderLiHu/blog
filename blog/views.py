from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
import markdown
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

# Create your views here.


def index(request):
    post_list = Post.objects.all()
    return render(request,
                  'blog/index.html',
                  context={
                      'title': '李虎的博客首页',
                      'post_list': post_list
                  })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'extra', # 包含下面7个子项
            # 'abbr', # Abbreviations
            # 'attr_list', # Attribute Lists
            # 'def_list', # Definition Lists
            # 'fenced_code', # Fenced Code Blocks
            # 'footnotes', # Footnotes
            # 'md_in_html', # Markdown in HTML
            # 'tables', # Tables
        'admonition', # Admonition
        'codehilite', # CodeHilite
        # 'legacy_attrs', # Legacy Attributes
        # 'legacy_em', # Legacy EM
        'meta', # Meta-Data
        # 'nl2br', # New-Line-to-Break Extension
        'sane_lists', # Sane Lists
        # 'smarty', # SmartyPants
        'toc', # Table of Contents
        # 
        # from markdown.extensions.wikilinks import WikiLinkExtension  # WikiLinks
        # WikiLinkExtension(base_url='/wiki/', end_url='.html')
        # TocExtension(slugify=slugify),
    ])
    post.text = md.convert(post.text)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', {"post": post})


def archive(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tag=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
