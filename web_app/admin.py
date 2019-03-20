from django.contrib import admin
from web_app.models import Post, Comment, UserProfile


# Add in this class to customise the Admin Interface
class PostAdmin(admin.ModelAdmin):
	list_display = ('postId','title','text','location','userId','image')
class CommentAdmin(admin.ModelAdmin):
	list_display = ('commentId','text','date','userId','postId')
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(UserProfile)