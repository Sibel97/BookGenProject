from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
from application import app
import pytest

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_genre(self):
       with patch('random.choice') as r:
           r.return_value = "Horror"
           response = self.client.get(url_for('Genre'))
           self.assertEqual(response.status_code, 200)
           self.assertIn(b'Horror', response.data)