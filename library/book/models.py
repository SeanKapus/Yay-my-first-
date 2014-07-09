from django.db import models


class BlogPost(models.Model):
    blog = models.CharField(max_length=100)

    def __unicode__(self):
        return self.blog


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    blog = models.ForeignKey(BlogPost)

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=100)
    comment = models.ForeignKey(Author)

    def __unicode__(self):
        return self.comment


class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=140)
    tag = models.ManyToManyField(Comment)

    def __unicode__(self):
        return u"{}".format(self.name)

