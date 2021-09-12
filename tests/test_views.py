from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'userName': 'mantra',
            'email': 'mantra@example.com',
            'password1': 'test123',
            'password2': 'test123'
        }
        self.cliente = Client()
    def test_home(self):
        request = self.cliente.post('home',data=self.dados)
        self.assertEquals(request.status_code,200)
        context = request
        self.assertEquals(context,request)
    def test_register(self):
        request = self.cliente.post(reverse_lazy('register'),data=self.dados)
        self.assertEquals(request.status_code,200)
        
class VerificationViewTestCase(TestCase):
    
    def setUp(self):
        self.request_data = {
                'username': 'mantra',
                'email': 'mantra@example.com',
                'password1': 'test123',
                'password2': 'test'
        }
        self.cliente = Client()
    
    def test_get(self):
        request = self.cliente.get(reverse_lazy('login'),data=self.request_data)
        self.assertEquals(request.status_code,200)

    def test_logout_request(self):
        logout_request = self.cliente.post(reverse_lazy('logout'))
        self.assertEquals(logout_request.status_code, 302)

    def test_delete_account(self):   
        
        self.request = self.cliente.get('home',data=self.request_data)
        self.assertEquals(self.request.status_code, 200)
    
    def test_login_request(self):
        self.request = self.cliente.get(reverse_lazy('login'),data=self.request_data)
        self.assertEquals(self.request.status_code, 200)
    
    def test_emergency_contact(self):
        context = {
            "contacts": '82666',
            "total_contacts": '82666,86665,46845,216486',
            "user": "mantra mori"
        }
        request = self.cliente.post('emergency_contact',data=context)
        self.assertEquals(request.status_code,200)

    def test_create_contact(self):
        self.request = self.cliente.get('create_contact',data=self.request_data)
        self.assertEquals(self.request.status_code, 200)

    def test_update_contact(self):
        self.request = self.cliente.get('update_contact',data=self.request_data)
        self.assertEquals(self.request.status_code, 200)
    
    def test_delete_contact(self):
        self.request = self.cliente.get('delete_contact',data=self.request_data)
        self.assertEquals(self.request.status_code, 200)
    
    def test_emergency(self):
        context = {
            "contacts": '82666',
            "total_contacts": '82666,86665,46845,216486',
            "user": "mantra mori"
        }
        request = self.cliente.post('emergency_contact',data=context)
        self.assertEquals(request.status_code,200)
    
    def test_change_password(self):
        request = self.cliente.post('change_password',data=self.request_data)
        self.assertEquals(request.status_code,200)

class HelpContactsViewTestCase(TestCase):
    def setUp(self):
        self.help_line_mock = {
            "Emergency": "911"
        }
        self.ngo_details_mock = {
            "Augustinho": "Carrara"
        }
        self.gallery_mock = {
            "Baianinha":"Abril de 2014"
        }
        self.faq_mock = {
            "Reclame Aqui": "..."
        }
        self.generics_mock = {
            "sieg":"heil"
        }

    def test_helpline_numbers(self):        
        request = self.client.post('helpline_numbers',data=self.help_line_mock)
        self.assertEquals(request.status_code,200)
    
    def test_ngo_details(self): 
        request = self.client.post('ngo_details',data=self.ngo_details_mock)
        self.assertEquals(request.status_code,200)
    
    def test_gallery(self):
        request = self.client.post('gallery',data=self.gallery_mock)
        self.assertEquals(request.status_code,200)

    def test_FAQ(self):
        request = self.client.post('FAQ',data=self.faq_mock)
        self.assertEquals(request.status_code,200)

    def test_women_laws(self):
        request = self.client.post('women_laws',data=self.generics_mock)
        self.assertEquals(request.status_code,200)
    
    def test_developers(self):
        request = self.client.post('developers',data=self.generics_mock)
        self.assertEquals(request.status_code,200)
    
    def test_women_rights(self): 
        request = self.client.post('women_rights',data=self.generics_mock)
        self.assertEquals(request.status_code,200)
    
    def test_page_not_found(self):
        request = self.client.post('404_error',data=self.generics_mock)
        self.assertEquals(request.status_code,200)

    def test_contact_user(self):
        request = self.client.post('contact_user',data=self.generics_mock)
        self.assertEquals(request.status_code,200)

    