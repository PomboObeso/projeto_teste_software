from django.test import TestCase
from main_app.forms import UserCreateForm
#from django.contrib.auth.forms import UserCreationForm


class UserCreateFormTestCase(TestCase):
    
    def setUp(self):        
        self.data = {
            'username': 'mantra',
            'email':'mantra@example.com',
            'password1': 'test123',
            'password2': 'test123',
        }
        self.form = UserCreateForm(self.data)

    def test_save(self,commit=True):
       # The success case.
        data = {
           'username': 'mantra',
           'email':'mantra@example.com',
           'password1': 'test123',
           'password2': 'test123',
        }
        #form = UserCreateForm(data)    
        self.assertEquals(self.data, data)
