from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.


class TestUrls:
    def test_detail_url(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'

