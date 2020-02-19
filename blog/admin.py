from django.contrib import admin
from .models import Category, Tag, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", "created_time", "modified_time", "category", "author"
    ]
    fields = ['title', 'text', 'excerpt', 'category', 'tag']

    # 改写ModelAdmin的save_model方法,每次通过admin后台更改post时,自动添加user
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
