
class Hexagon:
    def __init__(self, o):
        self.out = o
        
    def cal_perimeter(self):
        return self.out * 6


test_hexa = Hexagon (2)

print(test_hexa.cal_perimeter())
