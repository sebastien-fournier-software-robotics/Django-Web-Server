from django.urls import reverse
from rest_framework.test import APITestCase


class Part2TestCase(APITestCase):
    def assertFieldsAreIntegersOrFloats(self, data, fields):
        # Assert that specified fields in the dictionary have integer or floats values.
        for field in fields:
            self.assertIsInstance(data[field], (int, float))

    def test_get_exchange_data(self):
        url = reverse("exchangedata-get-exchange-data")
        response = self.client.get(url)

        expected_fields = ["bitcoin_eur", "bitcoin_gbp", "eur_to_gbp"]

        self.assertEqual(response.status_code, 200)
        self.assertFieldsAreIntegersOrFloats(response.json(), expected_fields)
