from flask import url_for
from flask_testing import TestCase
from datetime import date
import requests_mock
import pytest
from application import app 


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponseServiceOne(TestBase):
    
    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Book Generator', response.data)
        
    def test_generate(self):
        with requests_mock.Mocker() as m:
            m.get('http://Genre-api:5001/get_Genre', text='Horror')
            m.get('http://Author-api:5002/get_Author', text='Stephen King')
            m.post('http://Book-api:5003/get_Book', text='IT')
            
            response = self.client.get(url_for('Generate'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'IT', response.data)
            self.assertIn(b'Stephen King', response.data)
            self.assertIn(b'Horror', response.data)
