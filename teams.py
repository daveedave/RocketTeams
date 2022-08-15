import random

players = ("Tim", "Lukas","Adrian", "Felix", "David")
temp = []
teamsize = 3


for i in range(1000):
    tup = tuple(random.sample(players, teamsize))
    temp.append(tup)

     
team_1 = list({*map(tuple, map(sorted, temp))})
team_2 = []


for team in team_1:
    temp_2 = list(players)
    for name in team:
        temp_2.remove(name)     
    team_2.append(temp_2)



for i in range(len(team_1)):
    print("Runde : " + str(i + 1))
    print("Team 1 ist : " + str(team_1[i]) + " und Team 2 ist: " + str(team_2[i]))