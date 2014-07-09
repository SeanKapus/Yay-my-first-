from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import (Author,Tag,Post,User,Comment,Vote)

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Vote)
