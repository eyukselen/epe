import unittest
from datetime import datetime, timedelta
from eprofiler import timeit
import sys
import io


class TestTimeitDecorator(unittest.TestCase):

    def setUp(self):
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_duration_printed(self):
        @timeit()
        def test_function():
            return True

        test_function()
        printed_output = self.stdout.getvalue().strip()
        self.assertRegex(printed_output, r'^\d{0,2}:\d{0,2}:\d{0,2}')

    def test_duration_returned(self):
        stats = {}

        @timeit(stats)
        def test_function():
            for _ in range(1000000):
                pass

        test_function()
        self.assertTrue('start_time' in stats)
        self.assertTrue('end_time' in stats)
        self.assertTrue('duration' in stats)
        self.assertIsInstance(stats['start_time'], datetime)
        self.assertIsInstance(stats['end_time'], datetime)
        self.assertIsInstance(stats['duration'], timedelta)


if __name__ == '__main__':
    unittest.main()
