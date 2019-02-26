from django.contrib import admin
from web_app.models import Post, Comment, UserProfile


# Add in this class to customise the Admin Interface
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('postId',)}


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)