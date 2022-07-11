from django.test import TestCase

from car.forms.ServiceRequestForm import ServiceRequestForm


class ServiceRequestFormTestCase(TestCase):
    def test_should_pass_when_all_data_is_correct(self):
        data = {
            'message': "Custom message"
        }

        form = ServiceRequestForm(data=data)

        self.assertTrue(form.is_valid())

    def test_should_pass_when_message_is_not_provided(self):
        data = {
            'message': ""
        }

        form = ServiceRequestForm(data=data)

        expected_error = {
            'message': ['This field is required.']
        }

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, expected_error)
