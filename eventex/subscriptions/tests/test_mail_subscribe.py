from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        data = dict(name='Henrique Bastos',
                     cpf='12345678901', email='henrique@bastos.net', phone='21-996186180')
        
        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect,self.email.subject)
    
    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect,self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'henrique@bastos.net']
        
        self.assertEqual(expect,self.email.to)
    
    def test_email_body(self):

        contents = ['Henrique Bastos',
                    '12345678901',
                    'henrique@bastos.net',
                    '21-996186180']

        for content in contents:

            with self.subTest():
                self.assertIn(content,self.email.body)