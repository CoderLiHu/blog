from django.db import models
from django.utils import timezone


# Create your models here.
class Comment(models.Model):
    name = models.CharField('您的大名', max_length=50)
    email = models.EmailField('电子邮箱')
    url = models.URLField('个人网址', blank=True)
    text = models.TextField('您的留言')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('blog.Post',
                             verbose_name='文章',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return '{}.{}'.format(self.name, self.text[:20])
