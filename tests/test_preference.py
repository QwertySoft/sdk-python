import sys
sys.path.append('../')

import unittest

import mercadopago
from mercadopago.config import RequestOptions

class TestPreference(unittest.TestCase):
    sdk = mercadopago.SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_save_and_find(self):
        preference_object = {
            "items": [
                {
                    "description": "Test Save and Find",
                    "id": "1234",
                    "picture_url": "http://product1.image.png",
                    "quantity": 1,
                    "title": "Item 1",
                    "currency_id": "R$",
                    "unit_price": 10.4
                }
            ]
        }
        preference_saved = self.sdk.preference().create(preference_object)
        self.assertEqual(preference_saved["status"], 201)
        self.assertEqual(self.sdk.preference().get(preference_saved["response"]["id"])["status"], 200)

    def test_update_success(self):
        preference_object = {
            "items": [
                {
                    "description": "Test Update Success",
                    "id": "5678",
                    "picture_url": "http://product1.image.png",
                    "quantity": 1,
                    "title": "Item 1",
                    "currency_id": "R$",
                    "unit_price": 20.5
                }
            ]
        }
        preference_saved = self.sdk.preference().create(preference_object)
        self.assertEqual(preference_saved["status"], 201)

        preference_object["items"][0]["title"] = "Testando 1 2 3"

        preference_update = self.sdk.preference().update(preference_saved["response"]["id"], preference_object)

        self.assertEqual(preference_update["status"], 200)

        preference_saved = self.sdk.preference().get(preference_saved["response"]["id"])
        #self.assertEqual(preference_saved)

        self.assertEqual(preference_saved["response"]["items"][0]["title"], "Testando 1 2 3")

if __name__ == '__main__':
    unittest.main()
