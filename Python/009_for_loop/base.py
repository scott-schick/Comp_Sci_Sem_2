

x=int(input("Please enter the length of the line "))
y=str(input("Horizontal or vertical line? ")) 

for a in range(0,x+1):
    if(y == "horizontal"):
        print (a, end=" ")
    #print (4)
    elif(y == "vertical"):
        print(a)
    