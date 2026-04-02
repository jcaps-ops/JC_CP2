import random
import time
from faker import Faker
fake = Faker()
def race(horses):
    for x in horses:
        x[2] = x[4]
    racing = True
    while racing == True:
        for x in horses:
            x = raceturn(x)
            if x[3] >= 100:
                racing = False
        for x in horses:
            print(f"{x[0]}:Distance{x[3]}")
            if x[2] == 0:
                print(f"{x[0]}:State tired")
        time.sleep(1)
    for x in horses:
        if x[3] >= 100:
            print(f"{x[0]} Won the race")
            x[5] = x[5] + 1
        else:
            x[6] = x[6] + 1
        x[3] = 0
        x[2] = x[4]
    return horses

def horsecreation(count,maxspeed,maxstamina,horses):
    for x in range(0,count):
        temp = [fake.name(),random.randrange(maxspeed-5,maxspeed),0,0,random.randrange(maxstamina-5,maxstamina),0,0]
        horses.append(temp)
        print(temp)
    return horses


def raceturn(horse):
    if horse[2] > 0:
        for x in range(0,horse[2]):
            horse[3] = horse[3] + random.randrange(1,horse[1])
        horse[2] = horse[2] - 1
    else:
        horse[2] = horse[4]
    return horse


#Example horse [Name,Speed,stanmina,meter,maxstamina,wins,loses]
horses = horsecreation(5,10,10,[])
#horses = [["Dasher",5,7,0,7,0,0],["Prancer",7,5,0,5,0,0]]
for y in range(0,5):
    horses = race(horses)
    for x in horses:
        print(x)
    input("")