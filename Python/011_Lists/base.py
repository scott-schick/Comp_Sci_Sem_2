hahafunny = ["I was told to stop impersonating a flamingo. I had to put my foot down.", "I  was addicted to the hokey pokey, but then I turned myself around.", "Two fish are in a tank. One says, ‘How do you drive this thing?’", "Build a man a fire and he’ll be warm for a day. Set a man on fire and he’ll be warm for the rest of his life.", "The man who invented Velcro has died. RIP.", "The world champion tongue twister got arrested. I hear they’re going to give him a tough sentence.", "Communist jokes aren’t funny unless everyone gets them.", "A blind man walked into a bar… and a table… and a chair…", "I saw a sign the other day that said, ‘Watch for children,’ and I thought, ‘That sounds like a fair trade.’", "I have a few jokes about unemployed people, but none of them work.", ]

for x in range (0,100):
    z=str(input("funny????? "))
    if z == "yes":
        import random
        x=int(random.randrange(9))
        print(hahafunny[x])
    if z == "no":
        print("wrong answer ")