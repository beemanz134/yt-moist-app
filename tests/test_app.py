import sys
import os
import unittest
from flask import json
from src.app import app

class APItest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client = cls.app.test_client()

    def test_moist_inp_no_data(self):
        response = self.client.post('/inp', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'No data provided'})

    def test_moist_inp_invalid_data(self):
        response = self.client.post('/inp', json={'data': 'google.com'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid URL provided'})

    def test_moist_inp_valid_data(self):
        response = self.client.post('/inp', json={'data': 'https://www.youtube.com/watch?v=xxzw7-sCdnQ'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json)

    if __name__ == '__main__':
        unittest.main()