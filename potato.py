import random

def turn(grass_and_mud, second_die, destiny, potatos, orcs, cost):
    if grass_and_mud <=2:
        if second_die == 1:
            potatos += 1
        elif second_die == 2:
            potatos += 1
            destiny += 1
        elif second_die == 3:
            destiny += 1
            orcs += 1
        elif second_die == 4:
            orcs += 1
            potatos -= 1
        elif second_die == 5:
            potatos -= 1
        elif second_die == 6:
            potatos += 2
    elif grass_and_mud >=5:
        cost += 1
    else:
        if second_die == 1:
            orcs += 1
        elif second_die == 2:
            destiny += 1
        elif second_die == 3:
            orcs += 1
            destiny += 1
        elif second_die == 4:
            potatos -= 1
            orcs += 2
        elif second_die == 5:
            destiny += 1
        elif second_die == 6:
            potatos += 2
    return destiny, potatos, orcs, cost

burrow = 0
adventure = 0
dinner = 0
total = 10000
total_rounds = 0
for i in range(0,total):
    destiny = 0
    potatos = 0
    orcs = 0
    cost = 1
    while (destiny < 10 and potatos < 10 and orcs < 10):
        total_rounds += 1
        # while cost <= 1 and potatos >= 1 and orcs >= 1:
        # # while cost <= potatos and orcs >= 1:
        #     potatos -= cost
        #     orcs -= 1

        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        destiny, potatos, orcs, cost = turn(grass_and_mud=d1, second_die=d2, destiny=destiny, potatos=potatos, orcs=orcs, cost=cost)
        # print(destiny, potatos, orcs, cost)
    if destiny == 10:
        # print("Destiny")
        adventure += 1
    elif potatos >= 10:
        # print("Potatos")
        burrow += 1
    elif orcs >= 10:
        # print("Orcs")
        dinner += 1
print ("Orcs: {}, Potatos: {}, Destiny: {}".format(dinner, burrow, adventure))
print ("Orcs: {}%, Potatos: {}%, Destiny: {}%".format(100.*dinner/total, 100.*burrow/total, 100.*adventure/total))
print("Round Average: {}".format(total_rounds/total))