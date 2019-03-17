import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BringMeHome.settings')
import django

django.setup()
from web_app.models import Post, Comment ,  UserProfile
from django.contrib.auth.models import User

import datetime
from django.utils import timezone


def populate():
    python_posts = [
        {"Title": "Lost dog Number 1",
         "Text" : "I found this dog on the street",
         "Status" : "1",
         "UserId": "1",
         "postId":"1"},
         {"Title": "Lost dog Number 2",
         "Text" : "I found this dog on the sideway",
         "Status" : "1",
         "UserId": "2",
         "postId":"2"},
         {"Title": "Lost dog Number 3",
         "Text" : "Una doga perfecta",
         "Status" : "1",
         "UserId": "3",
         "postId":"3"}]



    python_comments = [
    {"Text" : "nice dog mate",
     "UserId": "petros",
     "commentid" : "1",
     "postId":"1"
    },
     {"Text" : "Wow mate",
     "UserId": "petros",
     "commentid" : "2",
     "postId":"2"
    }]
    
    for post in python_posts:
        add_post(post["Title"],
                 post["Text"],
                 post["Status"],
                 post["UserId"],
                 post["postId"])

    # for comm in python_comments:
    #     add_comm(comm["Text"],
    #              comm["UserId"],
    #              comm["commentid"],
    #              comm["postId"])

    # # Print out the categories we have added.
def add_post(title, text, status, UserId, postId):
    p = Post.objects.get_or_create(postId=postId)[0]
    p.title = title
    p.text = text
    p.status = status
    p.user = UserId
    p.save()
    return p

# def add_comm(text, UserId, commentid , postId):
#     c = Comment.objects.get_or_create(commentId = commentid)[0]
#     c.text = text
#     user = User.objects.get(id=UserId)
#     c.userId = userId
#     c.postId = postId
#     c.save()
#     return c



# Start execution here!
if __name__ == '__main__':
    print("Starting BringMeHome population script...")
    populate()
