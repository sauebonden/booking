from django.test import TestCase
from groups import views as group_views
from django.core.urlresolvers import reverse
from django.urls import resolve

class ListGroupLoggedOutTest(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    """
    def test_status_code(self):
        \"""
        test that view is login protected
        \"""
        self.assertEquals(self.response.status_code, 302)
    """

class ListGroupsLoggedInTest(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.login_response = self.client.login(email='jameshalpert@gmail.com',
                                                password='locoloco')
        url = reverse('home')
        self.response = self.client.get(url)

class NoListTest(ListGroupsLoggedInTest):
    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/')
        self.assertEquals(view.func, group_views.list_groups)