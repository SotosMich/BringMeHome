from django.conf.urls import url
from web_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^post/(?P<postId>[\w\-]+)/$', views.show_post, name='show_post'),
]