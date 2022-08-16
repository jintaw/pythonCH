import math

class Apple:
    def __init__(self, g , d , c, s):
        self.gram = g
        self.days = d
        self.color = c
        self.size = s

class Circle:
    def __init__(self , r):
        self.r = r
    
    def circle_area(self):
        return self.r **2 * math.pi



test_circle = Circle(5)
print(test_circle.circle_area())


