from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        data = dict(name='Pedro Prata',
                     cpf='46890347889', email='contato.pedroprata@gmail.com', phone='17981107024')
        
        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect,self.email.subject)
    
    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect,self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'contato.pedroprata@gmail.com']
        
        self.assertEqual(expect,self.email.to)
    
    def test_email_body(self):

        contents = ['Pedro Prata',
                    '46890347889',
                    'contato.pedroprata@gmail.com',
                    '17981107024']

        for content in contents:

            with self.subTest():
                self.assertIn(content,self.email.body)