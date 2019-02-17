import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BringMeHome.settings')
import django

django.setup()
from web_app.models import Post, Comment
import datetime
from django.utils import timezone


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    comments = [
        {"commentid": 1, "text": "kjasakjs", "date": "2019-02-05 00:00:00+00:00"},
        {"commentid": 2, "text": "dfgd", "date": "2019-02-05 00:00:00+00:00"}]

    posts = {1: {"comments": comments, "date": "2019-02-05 00:00:00+00:00", "text": "dsadada", "status": False}}

    # If you want to add more catergories or pages,
    # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for post, post_data in posts.items():
        p = add_post(post, post_data["date"], post_data["text"], post_data["status"])
        for c in post_data["comments"]:
            add_comment(p, c["commentid"], c["text"], c["date"])

    # # Print out the categories we have added.
    # for p in Post.objects.all():
    #     for c in Comment.objects.filter(postId=p):
            # print("- {0} - {1}".format(str(p), str(c)))


def add_comment(postid, commentid, text, date):
    c = Comment.objects.get_or_create(postId=postid, commentId=commentid)[0]
    c.text = text
    c.date = date
    c.save()
    return c


def add_post(postid, date, text, status):
    p = Post.objects.get_or_create(postId=postid)[0]
    p.date = date
    p.text = text
    p.status = status
    p.save()
    return p


# Start execution here!
if __name__ == '__main__':
    print("Starting BringMeHome population script...")
    populate()