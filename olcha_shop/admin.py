from django.contrib import admin

from olcha_shop.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Group)

admin.site.register(Value)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Attribute)
admin.site.register(Key)

