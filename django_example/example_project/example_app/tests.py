from django.test import TestCase
from fixtureless import Factory

from example_app.views import FibNumView
from example_app.models import FibHistory


class SuperSnazzyViewTests(TestCase):
    def setUp(self):
        self.factory = Factory()
        self.fib_num_view = FibNumView()

    def test_fib(self):
        expected_value = 0
        self.assertEqual(self.fib_num_view.fib(0), expected_value)


class SuperSnazzyModelTests(TestCase):
    def setUp(self):
        self.factory = Factory()

    def test_sum_fib_nums(self):
        initial = {
            'fib_index': 0,
            'fib_num': '1000',
        }
        fib_history = self.factory.create(FibHistory, initial)
        self.assertEqual(fib_history.do_something_pointless(), 0)

        initial = {
            'fib_index': 100,
            'fib_num': 10,
        }
        fib_history = self.factory.create(FibHistory, initial)
        self.assertEqual(fib_history.do_something_pointless(), 1000)
