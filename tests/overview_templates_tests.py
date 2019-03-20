
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
import os

from django.contrib.staticfiles import finders




class ViewTest(TestCase):

	def test_index_using_template(self):
		response = self.client.get(reverse('index'))

		# Check the template used to render index page
		self.assertTemplateUsed(response, 'web_app/index.html')

	def test_about_using_template(self):
		self.client.get(reverse('index'))
		response = self.client.get(reverse('about'))

		# Check the template used to render about page
		self.assertTemplateUsed(response, 'web_app/about.html')
		
		
	def test_login_using_template(self):
		self.client.get(reverse('index'))
		response = self.client.get(reverse('login'))

		# Check the template used to render about page
		self.assertTemplateUsed(response, 'web_app/login.html')

	def test_register_using_template(self):
		self.client.get(reverse('index'))
		response = self.client.get(reverse('register'))

		# Check the template used to render about page
		self.assertTemplateUsed(response, 'web_app/register.html')
		
	def test_found_posts_using_template(self):
		self.client.get(reverse('index'))
		response = self.client.get(reverse('found_posts'))

		# Check the template used to render about page
		self.assertTemplateUsed(response, 'web_app/found_posts.html')
		
	def test_lost_posts_using_template(self):
		self.client.get(reverse('index'))
		response = self.client.get(reverse('lost_posts'))

		# Check the template used to render about page
		self.assertTemplateUsed(response, 'web_app/lost_posts.html')
		
 


