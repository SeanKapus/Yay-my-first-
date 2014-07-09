__author__ = 'CatsAir'
from blog.models import Tag

# Get the tag with pk 1
tag = Tag.objects.get(pk=1)

# Get all of the posts with this tag
tag.posts.all()

# Get all tags on posts written by author id 1
tags = Tag.objects.filter(post__author_id=1)

# For each tag print out all of their posts names
for tag in Tag.objects.all():
    print tag.name
    for post in tag.posts.all():
        print post.title