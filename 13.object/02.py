
class Shape:
    def what_am_i(self):
        print("i am a shape")

class Rectangle(Shape):
    pass
    
class Square(Shape):
    pass

a_rec = Rectangle()
a_rec.what_am_i()
    
a_squ = Square()
a_squ.what_am_i()
    
