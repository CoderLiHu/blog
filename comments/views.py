from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from django.views.decorators.http import require_POST
from .forms import CommentForm
from django.contrib import messages

# Create your views here.


@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    form = CommentForm(request.POST)

    if form.is_valid():
        # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(request,
                             messages.SUCCESS,
                             "评论发表成功!",
                             extra_tags='success')
        url = post.get_absolute_url() + '#comment-' + str(comment.id)
        return redirect(url)

    context = {'form': form, 'post': post}
    messages.add_message(request,
                         messages.ERROR,
                         '评论发表失败！请检查表单。',
                         extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)
