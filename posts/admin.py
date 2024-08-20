from django.contrib import admin

from olcha_shop.models import Category
from posts.models import Post, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)