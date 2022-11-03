from hello import f1
import unittest
class TestHello(unittest.TestCase):
    def test_f1(self):
        flag=f1(1600)
        self.assertTrue(flag)
        
unittest.main()