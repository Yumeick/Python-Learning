from Pager import Pager
import unittest
class Test_Pager(unittest.TestCase):
    def setUp(self):
        self.pager1=Pager(101,10,5)
        
    def test_nextPage(self):
        self.pager1.setI(11)
        pageNum=self.pager1.nextPage()
        self.assertEqual(11,pageNum)
        
    def test_prePage(self):
        self.pager1.setI(1)
        pageNum=self.pager1.prePage()
        self.assertEqual(1,pageNum)
        
unittest.main()