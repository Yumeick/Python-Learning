import math
class Pager():        
    def __init__(self, sum, d, i):
        self.sum= sum
        self.d= d
        self.i= i
        
    def setI(self,j):
        self.i=j
        
    def nextPage(self):
        if self.i==math.ceil(self.sum/self.d):
            return self.i
        else:
            return self.i+1
        
    def prePage(self):
        if self.i==1:
            return self.i
        else:
            return self.i-1