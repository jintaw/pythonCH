from turtle import shape


class Shape:
    def __init__(self , h , t):
        self.height = h 
        self.tail = t
        
    def what_am_i():
        print("i am a shape")


class Rectangle:
    def __init__(self , h , t):
        self.height = h
        self.tail = t
        
    def caldulate_perimeter(self):
        return self.tail * 3
    
class Square:
    def __init__(self , h , t):
        self.height = h
        self.tail = t
        
    def caldulate_perimeter(self):
        return self.height * 2 +  self.tail * 2
    
    def change_size(self , new):
        self.height = new
    
a_rec = Rectangle(2,3)
print(a_rec.caldulate_perimeter())

a_squ = Square(2 , 3)
print(a_squ.caldulate_perimeter())
    
a_squ.change_size(100)
print(a_squ.height)

