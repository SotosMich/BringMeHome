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
        {"Title": "I found this cute dog",
         "Text" : "I found this dog wandering arround near Odos Pentelis. It seems injured, please contact me as soon as posible !!! ",
         "Status" : "1",
         "UserId": "1",
         "location" : "Odos Pentelis 10, Marousi, Greece",
         "image": "post_images/found_dog1.jpg"},

         {"Title": "I lost my dog",
         "Text" : "I lost my little buddy near my home, his name is Bruno, I am so sad, help me find my little boy :( ",
         "Status" : "2",
         "UserId": "1",
         "location" : "Ippokratous 10, Athens, Greece",
         "image": "post_images/lost_dog1.jpg"},

        {"Title": "I found a dog in Thessaloniki",
         "Text" : "Guys emergency! I found this dog on Aristotelous Square while I was going back home and I carried it home, please if you are interesetd , get in touch with me asap.",
         "Status" : "1",
         "UserId": "2",
         "location" : "Aristotelous Square, Thessaloniki, Greece",
         "image": "post_images/found_dog2.jpg"},

         {"Title": "We lost our family dog",
         "Text" : "We lost our family dog in the city centre Gounari, please contact us if you find our dog!",
         "Status" : "2",
         "UserId": "1",
         "location" : "Dim. Gounari 101, Thessaloniki, Greece",
         "image": "post_images/lost_dog2.jpg"},

        {"Title": "I found this dog on the city centre",
         "Text" : "I found this dog near Ampelokipous Metro station. If you know the owner just send me a message or give me a call. Don't worry, I ensure you she is safe!",
         "Status" : "1",
         "UserId": "3",
         "location" : "Panormou 9, Athens, Greece",
         "image": "post_images/found_dog3.jpg"}]



    python_comments = [
        {"Text" : "Really lovely dog, I wanna keep it. It will be grateful if you give me more details! I am looking to hear news from you!",
         "UserId": "3",
         "postId":"1"
        },
        {"Text" : "I am interested in adopting this dog",
         "UserId": "2",
         "postId":"1"
        },
        {"Text" : "Hey, good news for you!!! I found your little dog near my house, please give me a call and we can arrange a meeting, for now I keep it at my home, it is safe, so keep calm! :) ",
         "UserId": "2",
         "postId":"2"
        }]

    python_userProfile = [
    {"phoneNumber": "6958858585",
     "location" : "Marousi, Greece",
     "UserId": "1"},
     {"phoneNumber": "698963258",
     "location" : "Thessaloniki, Greece",
     "UserId": "2"},
     {"phoneNumber": "356579845",
     "location" : "Athens,Greece",
     "UserId": "3"}]


    python_users = [
    {"first_name": "Petros",
     "last_name" : "Chatziioannou",
     "username": "pchatziio",
     "email" : "pchatziio@gmail.com",
     "password": "123456",
     "phoneNumber": "12345678",
     "location" : "Glasgow",
     "image": "profile_images/petros.jpg"},
    {"first_name": "Sotiris",
     "last_name" : "Michael",
     "username": "msotos",
     "email" : "msotiris@gmail.com",
     "password": "123456",
     "phoneNumber": "12345678",
     "location" : "Glasgow",
     "image": "profile_images/sotos.png"},
    {"first_name": "Harry",
     "last_name" : "Konstantinidis",
     "username": "kharry",
     "email" : "kharry@gmail.com",
     "password": "123456",
     "phoneNumber": "12345678",
     "location" : "Glasgow",
     "image": "profile_images/harrys.jpg"}]


    
    for user in python_users:
       add_user(user["first_name"],
                 user["last_name"],
                 user["username"],
                 user["email"],
                 user["password"],
                 user["phoneNumber"],
                 user["location"],
                 user["image"])

    for post in python_posts:
        add_post(post["Title"],
                 post["Text"],
                 post["Status"],
                 post["UserId"],
                 post["location"],
                 post["image"])

    for comm in python_comments:
        add_comm(comm["Text"],
                 comm["UserId"],
                 comm["postId"])

def add_user(firstName, lastName, userName, email, password, phoneNumer , location, image):
    u = User.objects.create(first_name=firstName , last_name=lastName, username = userName , email= email, password = password)
    u.set_password(password)
    u.save()
    uP = UserProfile.objects.create(phoneNumber = phoneNumer, user=u, location=location, photo=image)  
    return (u,uP)

def add_post(title, text, status, UserId,location, image):
    p = Post.objects.create(title=title, text=text, status=status, location=location, userId=User.objects.get(pk=UserId), image=image)
    return p

def add_comm(text, UserId, postId):
    c = Comment.objects.create(text=text, userId=User.objects.get(pk=UserId), postId=Post.objects.get(pk=postId))
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting BringMeHome population script...")
    populate()
