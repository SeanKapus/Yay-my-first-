from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=120)
    twitter = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return u"{}".format(self.name)

class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(Author, related_name='posts')

    def __unicode__(self):
        return u"{}".format(self.title)

class Tag(models.Model):
    name = models.CharField(max_length=20)
    posts = models.ManyToManyField(Post)

    def __unicode__(self):
        return u"{}".format(self.name)


###################homeworks######################################

class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    username = models.CharField(max_length= 120)
    #like = models.ManyToManyField(Post, related_name= 'likes')


    def __unicode__(self):
        return u"{}".format(self.username)

class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, related_name='user_comment')
    post = models.ManyToManyField(Post, related_name='comments')

    def __unicode__(self):
        return u"{}".format(self.body)

class Vote(models.Model):
    user = models.ForeignKey(User, related_name='user_vote')
    post = models.ForeignKey(Post, related_name='vote_comment')
