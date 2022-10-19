import unittest
from combineorders.orders import Orders


class TestCombineOrders(unittest.TestCase):

    def setUp(self):
        self.orders = [70, 30, 10]
        self.n_max = 100
        self.expected_orders = 2

    def test_combine_orders(self):

        how_many = Orders().combine_orders(self.orders, self.n_max)
        self.assertEqual(self.expected_orders, how_many)
        self.assertIsInstance(how_many, int)
