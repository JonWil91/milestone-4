from django.test import TestCase
from .forms import CommentForm


class TestContactForm(TestCase):

    # check to see if required fields are set as required
    def test_comment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    # check that only fields within form are displayed in case of addition to the model
    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['body'])
