class Horse:
    def __init__(self , name , owner):
        self.name = name
        self.owner = owner
               
        
class Rider:
    def __init__(self, name ):
        self.name = name 
        

arima = Rider("arima")
usa = Horse("usagi" , arima)
    

print(usa.owner.name)

