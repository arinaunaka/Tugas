from django.test import TestCase, Client
from django.urls import reverse

class TestUrls(TestCase):
    def test_html_url(self):
        response = Client().get(reverse("mywatchlist:show_html"))
        self.assertEquals(response.status_code, 200)

    def test_json_url(self):
        response = Client().get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code, 200)

    def test_xml_url(self):
        response = Client().get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code, 200)