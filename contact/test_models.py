from django.test import TestCase
from .models import Contact


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Contact.objects.create(name='Test Todo Contact')
        self.assertFalse(item.name)
