from re import A, S


class Square:
    square_list = []
    
    def __init__(self , w ,l):
        self.width = w
        self.len = l
        self.square_list.append([self.width , self.len])
    
    def print_four(self):
        print("{} by {} by {} by {}".format(self.width , self.width, self.width, self.width))


s1= Square(100,1)
s2 = Square(2,2)
s3 = Square(3,3)

print(Square.square_list)
s1.print_four()
