x=int(input("Please enter a number "))
c=str(input("Please enter an operation "))
y=int(input("Please enter a second number "))

if(c=="+"):
    z=int(x+y)
    print(str(x) + str(c) + str(y) + "=" + str(z))
elif(c=="-"):
    z=int(x-y)
    print(str(x) + str(c) + str(y) + "=" + str(z))
elif(c=="*"):
    z=int(x*y)
    print(str(x) + str(c) + str(y) + "=" + str(z))
elif(c=="/"):
    z=int(x/y)
    print(str(x) + str(c) + str(y) + "=" + str(z))