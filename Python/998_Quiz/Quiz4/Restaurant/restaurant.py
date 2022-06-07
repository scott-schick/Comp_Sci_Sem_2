shops = ["Tickle Tree", "McDonald's", "Black Cow"]
Tickle = ["BLAT", "Mint Lemonade", "Pasta"]
MCD = ["Big Mac", "Apple Pie", "Fries"]
Black = ["Chili-stuffed Skillet", "Buttermilk Pancakes", "biscuits"]

print(shops)
a = input(int(" Which restaurant would you like to go to?"))

if a == "Tickle Tree":
    import random 
    t = random.randrange(3)
    print(Tickle)
    print(Tickle[t])

elif a == "McDonald's":
    import random 
    m = random.randrange(3)
    print(MCD)
    print(MCD[m])

elif a == "Black Cow":
    import random 
    b = random.randrange(3)
    print(Black)
    print(Black[b])