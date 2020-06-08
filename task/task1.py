def fibs(n):
    prev, current = 0, 1
    fibs = []
    for i in range(n):
        fibs.append(current)
        prev, current = current, prev+current
    print('Sequences : ',fibs)
    print('Series : ',fibs[i])

def starLoop(a):
    for x in range(1,a+1):
        for y in range(1,x+1):
            print('*', end="")
        print()

def selectPrograms(userInput):
    if userInput==1:
        a = int(input("Please enter amount of stars to loop : "))
        starLoop(a)
    elif userInput==2:
        n = int(input("Please enter Fibonacci number : "))
        fibs(n)
    else:
        print('Please enter valid input.')

print(' 1 : Starloop program \n 2 : Fibonacci number')
userInput = int(input("Select programs number : "))
selectPrograms(userInput)