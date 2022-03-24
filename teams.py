import random

players = ("David", "Raphi", "Lukas","Adrian", "Felix")
temp = []
teamsize = 2


for i in range(100):
    
    tup = tuple(random.sample(players, teamsize))
    temp.append(tup)
       
teams = list({*map(tuple, map(sorted, temp))})

print(teams)