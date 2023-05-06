import unittest
from server import supported_currencies, convert, convert_all


class CurrencyConverterTests(unittest.TestCase):
    def test_supported_currencies(self):
        currencies = supported_currencies()
        self.assertIsInstance(currencies, list)

    def test_convert(self):
        convert_response = convert("USD", 100.50, "CAD")
        self.assertIsInstance(convert_response.__dict__, dict)
        self.assertEqual(convert_response.currency, "CAD")
        self.assertIsInstance(convert_response.amount, float)

    def test_convert_all(self):
        convert_response = convert_all("USD", 100.50)
        self.assertIsInstance(convert_response, list)


if __name__ == "__main__":
    unittest.main()
