from django.contrib import admin
from book.models import BlogPost, Author, Comment, Tag


admin.site.register(BlogPost)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Tag)
