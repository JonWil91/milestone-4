from django.test import TestCase


class TestContactViews(TestCase):

    def test_get_contact_page(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
