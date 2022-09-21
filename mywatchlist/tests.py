from django.test import TestCase, Client
from django.urls import resolve
from mywatchlist.views import *

class TestUrls(TestCase):
    def test_html_url(self):
        response = Client().get('/mywatchlist/html')
        self.assertEquals(response.status_code, 200)

    def test_json_url(self):
        response = Client().get('/mywatchlist/json')
        self.assertEquals(response.status_code, 200)

    def test_xml_url(self):
        response = Client().get('/mywatchlist/xml')
        self.assertEquals(response.status_code, 200)