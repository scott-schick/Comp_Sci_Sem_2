mynumbers = [6,9,32,28,15,22,3,18]
x = 1
bigbase = mynumbers[x]
smalbase = mynumbers[x]

for x in range(0,len(mynumbers)):
    if mynumbers[x] == bigbase:
        bigbase = bigbase
    if mynumbers[x] == smalbase:
        smalbase = smalbase
    if mynumbers[x] > bigbase:
        bigbase = mynumbers[x]
    if mynumbers[x] < smalbase:
        smalbase = mynumbers[x]
    x=x+1
    
print("The maximum value is "+ str(bigbase))
print("The minimum value is "+ str(smalbase))

y = 1
total = 0
for y in range(0,len(mynumbers)):
    total = total + mynumbers[y]
    y=y+1

avrag = total/len(mynumbers)
print("The average value is "+str(avrag))
    
print ("hello")