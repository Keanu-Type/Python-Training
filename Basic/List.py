
#-------LIST-----------
name = ['a','b','c','d','e','f','g']
print(name[1])          #print a certain range(0-n)
print(name)             #print all
print(name[2:6])        #print the 2nd index-6th
print(name[:6])         #print from beginning to 6th index
print(name[2:])         #print 2nd index and so on


#Replacing value inside the list
name[0] ='jon'          #enter the index you want to replace in name[n] in the n
print(name[0])


#Printing largest number
number =[3,6,2,8,4,10]
max = number[0]
for x in number:
    if x > max:
        max = x
print(max)

#----------2D LIST--------
print("2D List")
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for row in matrix:
    for item in row:
        print(item)

matrix[1][1] = 20           #replacing number inside matrix
print(f" {matrix[0][1]}")
print(f"{matrix[1][1]}")

#---------LIST METHOD-----------
print("LIST METHOD")
print(" ")
numbers = [5,2,1,7,4]
numbers.append(20)          #add 20 at the End. Append = End
print(numbers)  
numbers.insert(0,10)        #add 10 at 0th index
print(numbers)
numbers.remove(5)           #remove certain value. removing 5 int      
print(numbers)  
numbers.clear()             #clear all data    
print(numbers)
numbers = [5,2,1,7,4,5,5,5,5]
print(numbers.index(5))     #shows the 5. it will show the first index it appear. 
                            #     5 appear on 0th index so this 5 comes from 0th index
print(50 in numbers)        #a true or false statement
print(numbers.count(5))     #count how many 5 there is inside
numbers.sort()              #sort ascending  
print(numbers)
number.reverse()            #sort descending
numbers2 = numbers.copy()   #copy all value
numbers2.append(10)         
print(numbers2)

#exercise. remove all copy number
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(f"uniques are: {uniques}")