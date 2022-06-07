randlist = [1,2,3,4,5,6,7,8,9,10]

for w in range(0,100):
    x=int(input("How many random numbers would you like? "))
    print("Your numbers are: ", end=" ")
    for i in range(0,x):
        import random
        i=int(random.randrange(10))
        print (randlist[i], end=" ")
    


    