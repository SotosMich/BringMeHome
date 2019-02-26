# Create your models here.
from django.db import models
# from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    # postId = models.ForeignKey(Category, on_delete=models.PROTECT)
    postId = models.AutoField(primary_key=True)
    # date = models.DateTimeField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=256)
    # image = models.ImageField(upload_to='post_images/')
    image = models.ImageField(upload_to='post_images/', 
        null=True, 
        blank=True)
    status = models.BooleanField(default=False)
    userId = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):  # For Python 2, use __unicode__ too
        return str(self.postId)


class Comment (models.Model):
    commentId = models.AutoField(primary_key=True)
    text = models.CharField(max_length=256)
    date = models.DateTimeField(max_length=50, null=True)
    userId = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    postId = models.ForeignKey(Post, on_delete=models.PROTECT, null=True)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    phoneNumber = models.IntegerField()
    location = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='profile_images/', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user
