class Point: #POINT
    def move(self): #blueprint of POINT
        print("move!")
    
    def draw(self): #blueprint of POINT
        print("draw")

point1 = Point() #declare point1 as Point1
point1.draw()   #call the blueprint related to draw

point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)

#CONSTRUCTOR
class Construct: #POINT
    def __init__(self): #CONSTRUCTOR
        pass
    def move(self): #blueprint of POINT
        print("move!")
    
    def draw(self): #blueprint of POINT
        print("draw")

