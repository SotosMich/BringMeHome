from django.conf.urls import url
from web_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^logout/$', views.user_logout, name='invalid'),
    url(r'found_posts/$', views.found_posts, name='found_posts'),
    url(r'lost_posts/$', views.lost_posts, name='lost_posts'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^post/(?P<postId>[\w\-]+)/$', views.show_post, name='show_post'),
    url(r'^map', views.map, name='map'),
    url(r'^profile/', views.view_profile, name='view_profile'),
    url(r'^user/(?P<userID>[\w\-]+)/$', views.view_user, name='view_user'),
    url(r'^delete/$', views.user_delete, name='delete'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),

]
