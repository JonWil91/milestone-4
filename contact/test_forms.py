from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    # check to see if required fields are set as required
    def test_contact_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # check that only fields within form are displayed in case of addition to the model
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.fields, ['name', 'email', 'message_title', 'message'])
