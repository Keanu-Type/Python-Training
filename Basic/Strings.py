print('Keanu')
print('Keanu ' * 10)  # String * number = multiplying text n times

#USE String[n:n]
course = 'python for beginners'
print(course[5:10])  #printing characters from 0th to 3rd character(including space)
print(course[5:]) #Printing characters from 5th charcter to end of text 
print(course[:5]) #Printing chracters from beginning to 5th character
print(course[:-9]) #print all except the last 9 character
#other idea:
     #course = course[5:10]  

print(course)

#FORMATTED STRING
first = 'Keanu'
last  = 'Berches'
msg = f'{first} [{last}] is a programmer' #so you can use {} inside
print(msg)

#CALCULATING THE LENGTH OF STRING
print(len(course))

#METHODS
#metho can be use by String.command() . note that the command() is not function. it is a method
print(course.upper())  #AUTOMATICALLY UPPERCASE EVERY CHARACTER
print(course.replace('python','C++')) #replacing specific text
print(course.find('o')) #finding which part of the text has 'o'

#converting string to Int
guess = int(input('guess number:'))