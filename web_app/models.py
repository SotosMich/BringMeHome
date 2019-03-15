# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    # postId = models.ForeignKey(Category, on_delete=models.PROTECT)
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=65, default="")
    # date = models.DateTimeField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=256)
    # image = models.ImageField(upload_to='post_images/')
    image = models.ImageField(upload_to='post_images/', 
        null=True, 
        blank=True)
    status = models.IntegerField(default=False)
    location = models.CharField(max_length=128, default="")
    # found = models.BooleanField(default=True)
    userId = models.ForeignKey(User, null=True)
    # slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.postId)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):  # For Python 2, use __unicode__ too
        return str(self.postId)


class Comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    text = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, null=True)
    postId = models.ForeignKey(Post, related_name='comments', null=True)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    phoneNumber = models.IntegerField()
    location = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='profile_images/', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return str(self.user)