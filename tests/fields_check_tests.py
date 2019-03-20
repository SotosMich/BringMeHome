# Chapter 3
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.core.urlresolvers import reverse
import os, socket


from django.contrib.staticfiles import finders


from web_app.models import Post, Comment
import population_script
import web_app.test_utils as test_utils


class LiveServerTests(StaticLiveServerTestCase):

    def setUp(self):
        from django.contrib.auth.models import User
        User.objects.create_superuser(username='admin', password='admin', email='admin@me.com')
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("test-type")
        #self.browser = webdriver.Chrome(chrome_options=chrome_options)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options = chrome_options)
        self.browser.implicitly_wait(3)

    @classmethod
    def setUpClass(cls):
        cls.host = socket.gethostbyname(socket.gethostname())
        super(Chapter5LiveServerTests, cls).setUpClass()

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_populationscript(self):
        #Populate database
        #population_script.populate()
        print("OMGDF")
        url = self.live_server_url
        #url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('admin:index'))

        # Log in the admin page
        test_utils.login(self)

        # Check the pages saved by the population script
        self.browser.get(url + reverse('admin:web_app_post_changelist'))
		
        self.browser.find_elements_by_partial_link_text('1')
        self.browser.find_elements_by_partial_link_text('2')
        self.browser.find_elements_by_partial_link_text('3')
        self.browser.find_elements_by_partial_link_text('4')
        self.browser.find_elements_by_partial_link_text('2')
		
        #

    def test_page_contains_all_fields(self):
        #population_script.populate()
        url = self.live_server_url
        url = url.replace('localhost','127.0.0.1')
        self.browser.get(url+ reverse ('admin:index'))
		
        test_utils.login(self)
        posts_link = self.browser.find_element_by_link_text('Posts')
        posts_link.click()
        body = self.browser.find_element_by_tag_name('body')
        posts = Post.objects.all()
        
        #posts = Post.objects.all()
        for post in posts:
            self.assertIn(post.title,body.text)
            self.assertIn(post.text,body.text)
            self.assertIn(post.location,body.text)
            self.assertIn(str(post.userId_id),body.text)
            self.assertIn(str(post.status),body.text)
            self.assertIn(str(post.postId),body.text)
			
			
			
    def test_admin_can_create_post(self):
        population_script.populate()
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('admin:index'))

        # Check if it display admin message
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # Log in the admin page
        test_utils.login(self)

        # the Site Administration page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        # Check if is there link to categories
        posts_link = self.browser.find_elements_by_partial_link_text('Posts')
        self.assertEquals(len(posts_link), 1)

        # Click in the link
        posts_link[0].click()

        # Empty, so check for the empty message
        body = self.browser.find_element_by_tag_name('body')
        #self.assertIn('0 posts', body.text.lower())

		##ADD new post
        new_poll_link = self.browser.find_element_by_class_name('addlink')
        new_poll_link.click()

        # Check for input field
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Title:'.lower(), body.text.lower())

        # Input category name
        post_field = self.browser.find_element_by_name('title')
        post_field.send_keys("new dog")

         # Gertrude clicks the save button
        save_button = self.browser.find_element_by_css_selector("input[value='Save']")
        save_button.click()

class ModelTests(TestCase):

    def test_comments_a_new_post(self):
        post = Post(title="I found this dog on the city centre",text = "I found this dog near the city centre of Glasgow")
        post.save()

        # Check post is in database
        posts_in_database = Post.objects.all()
        self.assertEquals(len(posts_in_database), 1)
        only_poll_in_database = posts_in_database[0]
        self.assertEquals(only_poll_in_database, post)
		
    def test_create_pages_for_categories(self):
        post = Post(title="I found this dog on the city centre",text = "I found this dog near the city centre of Glasgow",status=1)
        post.save()

        # create 2 comments for post "I found this dog on the city centre"
		
        first_comment = Comment()
        first_comment.post = post
        first_comment.text="New comm"
        first_comment.save()

        second_comment = Comment()
        second_comment.post = post
        second_comment.text="Second one"
        second_comment.save()
	