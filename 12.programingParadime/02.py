

from multiprocessing.heap import Arena


class Triangle:
    def __init__(self,t , h):
        self.teihen = t
        self.height = h
        
    def area(self):
        return self.teihen * self.height /2


test_triangle = Triangle(2 , 4)

print(test_triangle.area())

