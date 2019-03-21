# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    # postId = models.ForeignKey(Category, on_delete=models.PROTECT)
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=65, default="")
    # date = models.DateTimeField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=2000)
    # image = models.ImageField(upload_to='post_images/')
    image = models.ImageField(upload_to='post_images/', 
        null=True, 
        blank=True)
    status = models.IntegerField(default=False)
    location = models.CharField(max_length=128, default="")
    # found = models.BooleanField(default=True)
    userId = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
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
    userId = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, related_name='comments', null=True, on_delete=models.CASCADE)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    phoneNumber = models.IntegerField(default='0')
    location = models.CharField(max_length=250, default="Athens, Greece")
    photo = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return str(self.user)