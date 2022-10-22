import unittest
import main


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # run once before all test cases
        cls._main = main.Main(com="COM3")

    @classmethod
    def tearDownClass(cls):  # run once after all test cases
        pass

    def test_arduino(self):
        self._main.server_arduino()
