from django import forms
from .models import Comment
from django.utils.translation import ugettext_lazy as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text'] 
        labels = {
            'name': _('您的大名'),
            'email': _('电子邮箱'),
            'url': _('个人网址'),
            'text': _('您的留言'),

        }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        error_messages = {
            'name': {
                'required': _("名字不能为空"),
                'max_length': _("名字过长，请重新输入"),
            },
            'email': {
                'required': _("邮箱不能为空"),
                'invalid': _("邮箱格式不正确"),
                'max_length': _("邮箱过长，请重新输入"),
            },
            'text': {
                'required': _("留言内容不能为空"),
                'max_length': _("留言内容过长，请重新输入"),
            },
            'url': {
                'invalid': _("网址格式不正确"),
                'max_length': _("网址过长，请重新输入"),
            },
        }