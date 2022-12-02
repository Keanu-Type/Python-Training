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

#----------CONSTRUCTOR-------
class Construct: #POINT
    def __init__(self, x, y): #CUSTOM  MAKING CONSTRUCTOR
        self.x = x
        self.y = y 
    def move(self): #blueprint of POINT
        print("move!")
    
    def draw(self): #blueprint of POINT
        print("draw")


point = Construct(10,20)
#you dont need to put self.x = 10 and self.y manually
print(point.x)
print(point.y)

#make a constructor with person:
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hello!{self.name}") #you can call other blueprint/constructor inside this classes

user = Person("Keanu") #default, will be plased on def  __init__
print(user.name) #check if the Keanu assigned to def __init__
user.talk()

#-------INHERITANCE-------------
#example:
class DogA:
    def walk(self):
        print("walk") #this is bad. we have duplicate with Cat class with same purpose

class CatA:
    def walk(self):
        print("walk") #this is bad. we have duplicate with Dog class with same purpose

#in inheritance. we can inherit same def/construcotr in different classes
#HOW TO INHERTIANCE

class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("woof woof") 

class Cat(Mammal):
    pass # pass means, hey pass this line, ignore this. we can get error since we have class BUT without its own constructor.

dogs = Dog()
dogs.walk()
dogs.bark()
cats = Cat()
cats.walk()
