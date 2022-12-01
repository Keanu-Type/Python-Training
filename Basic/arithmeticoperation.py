#CASTING

x = int(100) #x = 100
x2 = int(7)   
y = str(100)   #y = '100'
z = float(100) #z = 100.0

#ARITHMETIC OPERATION
print(x+x2)   #Addition
print(x-x2)   #Subtraction
print(x/x2)   #Division
print(x//x2)  #Division WITHOUT .3333
print(x % x2) #Division Modulus. returns only the remainder
print(x*x2)   #Multiplication
print(x**x2)  #Exponent. X is the main number. xx2 is the exponent

#AUGEMENTED OPERATION
#regular expression
t = 10
t = t+3
#augemented expression
t+=3  #its basically t=t+3, but simpler. you can also do t-=t+3 etc

#converting
t = 2.9
print(round(t)) #return 3 instead of 2.9
#absolute
print(abs(-2.9)) #return 2.9 instead of -2.9

import math #allows you to access more mathematic operation(acos, sin, tan etc)