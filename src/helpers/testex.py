import json
import unittest
from __init__ import app

app.testing = True

class MyTestCase(unittest.TestCase):
    def test_login(self):
        with app.test_client() as client:
            with self.subTest():
                data = {'id': 1}
                sent = json.dumps(data)
                result = client.post(
                    '/login',
                    data=sent, headers={'Content-Type': 'application/json'})
                print(result.data)

    def test_register(self):
        with app.test_client() as client:
            with self.subTest():
                data = {'id': "haya", "name": "yaser", "type": "owner"}
                sent = json.dumps(data)
                result = client.post(
                    '/register',
                    data=sent, headers={'Content-Type': 'application/json'})
            print(result.data)


if __name__ == '__main__':
    unittest.main()
