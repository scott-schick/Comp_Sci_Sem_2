
people = ["Dentist ", "Brother ", "Kanye West ", "Eunju "]
compliment = ["is cool", "is very cool", "is really cool", "is super duper cool"]

import random
num_people = random.randrange(0,len(people_list))
num_comp = random.randrange(0,len(comp_list))

print(people[num_people]+compliment[num_comp])


