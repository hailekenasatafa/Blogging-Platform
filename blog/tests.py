from django.test import TestCase
from rest_framework.test import APIClient

class BlogPostTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_blog_post(self):
        response = self.client.post('/api/posts/', data={"title": "Test Post"})
        self.assertEqual(response.status_code, 201)
