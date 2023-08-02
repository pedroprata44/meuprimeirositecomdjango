from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_has_fields(self):
        ''' Form must have 4 fields. '''
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_cpf_is_digit(self):
        ''' CPF must only accpet digits '''
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertErrorCode(form, 'cpf', 'digits')


    def test_cpf_has_11_digits(self):
        ''' CPF must have eleven digits '''
        form = self.make_validated_form(cpf=1234)

        self.assertErrorCode(form, 'cpf', 'lenght')
    
    def test_must_be_captalize(self):
        ''' Name must be captalized '''
        #HENRIQUE Bastos -> Henrique Bastos

        form = self.make_validated_form(name='HENRIQUE Bastos')
        self.assertEqual('Henrique Bastos', form.cleaned_data['name'])

    def test_email_is_optional(self):
        ''' Email is optional '''
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)
    
    def test_phone_is_optional(self):
        ''' Phone is optional '''
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)
    
    def test_must_email_or_phone(self):
        ''' Email or phone are optional, but one must be informed '''
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertErrorCode(self, form, field, code):    
        errors = form.errors.as_data()
        errors_list = errors[field]
        expection = errors_list[0]
        self.assertEqual(code, expection.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)
    
    def make_validated_form(self, **kwargs):
        valid = dict(name='Henrique Bastos', cpf='12345678901',
                    email='henrique@bastos.net', phone='996186810')

        data = dict(valid, **kwargs)

        form = SubscriptionForm(data)
        form.is_valid()

        return form