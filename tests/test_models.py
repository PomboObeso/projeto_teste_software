from django.test import TestCase
from model_mommy import mommy

class ContactTestCase(TestCase):
    
    def setUp(self):
        self.contato = mommy.make('contact')

    def test_str(self):
        self.assertEquals(str(self.contato), self.contato.name)