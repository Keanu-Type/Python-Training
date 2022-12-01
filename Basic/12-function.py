#VOID FUNCTION
def greet_user(name):
    print(f'hello {name}!')
    print('hello{name}!') #use print(f'string') or else the name wont appear(run it to see)

def position(first, second):
    print(f'First: {first} | Second: {second}')


greet_user("keanu")
position("2nd","1st") #non specified adjusting position
position(second="2nd", first="first") #specifically adjusting position


#RETURN FUNCTION
def maths(sumA, sumB):
    return (sumA + sumB)

print(maths(sumB=10,sumA=20))
