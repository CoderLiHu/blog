from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import strip_tags
from django.urls import reverse
import markdown


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField("标题", max_length=70)
    text = models.TextField("内容", )
    created_time = models.DateTimeField("创建时间", default=timezone.now)
    modified_time = models.DateTimeField("修改时间", )
    excerpt = models.CharField("摘要", max_length=200, blank=True)

    category = models.ForeignKey(Category,
                                 verbose_name="分类",
                                 on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name="标签", blank=True)
    author = models.ForeignKey(User,
                               verbose_name="作者",
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-created_time', 'title']

    # 改写save,每次保存时更新modified_time
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        self.excerpt = strip_tags(md.convert(self.text))[:54]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
