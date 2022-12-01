is_hot = True

#IF and ELIF STATEMENT
if is_hot==True:
    print("Hot")   #indent is important
elif is_hot == False:
    print("not hot")

print("enjoy day")

#WHILE LOOP STATMENT
i = 1
while i<= 5:
    print(i)
    i=i+1

    if i == 3:
        break #break means end the loop promptly
print("done")


#FOR LOOP STATEMENT

for item in 'python':
    print(item) #printing Each Letter in Python

#List Loop
for item in ['Mosh','Keanu','Juka']:
    print(item)

#Range Loop
for item in range(10):
    print (item)

#list add loop
prices = [10,20,30]
total = int()

for price in prices:
    total += price

print(f"total is {total}")

#NESTED LOOP(LOOP INSIDE A LOOP)
for x in range(6):
    for y in range(6):
        print(f"({x}, {y})")