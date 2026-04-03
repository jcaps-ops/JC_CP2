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
            time.sleep(0.2)
        input("")
    for x in horses:
        if x[3] >= 100:
            print(f"{x[0]} Won the race")
            x[5] = x[5] + 1
        else:
            x[6] = x[6] + 1
        x[3] = 0
        x[2] = x[4]
    return horses

def raceturn(horse):
    if horse[2] > 0:
        for x in range(0,horse[2]):
            horse[3] = horse[3] + random.randrange(1,horse[1])
        horse[2] = horse[2] - 1
    else:
        horse[2] = horse[4]
    return horse


def horsecreation(count,maxspeed,maxstamina,horses):
    for x in range(0,count):
        first = fake.catch_phrase()
        first = first.split(" ")
        first = first[0]
        second = fake.name()
        second = second.split(" ")
        second = second[1]
        skill = skillCreations()
        temp = [first + " " + second,random.randrange(maxspeed-5,maxspeed),0,0,random.randrange(maxstamina-5,maxstamina),0,0,skill[0],skill[1],skill[2],False]
        horses.append(temp)
        print(temp)
    return horses
def skillCreations():
    skillactTypes = ["Start","Middle","End"]
    skilleffTypes = ["Speed","Max stamina","Stamina","Meter"]
    skillactTypes1 = skillactTypes[random.randrange(0,2)]
    skilleffTypes1 = skilleffTypes[random.randrange(0,3)]
    #rand_Prefix = fake.catch_phrase()
    #print(rand_Prefix)
    #rand_Prefix.split(" ")
    #rand_Prefix_1 = rand_Prefix[0]
    #print(rand_Prefix_1)
    rand_color = fake.color_name()
    randplace = fake.city()
    effect_name = ''
    if skilleffTypes1 == "speed" or skilleffTypes1 == "Meter":
        effect_name = "Dash"
    elif skilleffTypes1 == "Max stamina":
        effect_name = "Improvement"
    elif skilleffTypes1 == "Stamina":
        effect_name = "Recovery"
    
    skill_name = rand_color + " " + randplace + " "+ effect_name
    return [skillactTypes1,skilleffTypes1,skill_name]


#Example horse [Name,Speed,stanmina,meter,maxstamina,wins,loses,Skill activation,Skill effect, Skill name,Has activated skill]
horses = horsecreation(5,10,10,[])
#horses = [["Dasher",5,7,0,7,0,0],["Prancer",7,5,0,5,0,0]]
skillCreations()
for y in range(0,5):
    horses = race(horses)
    for x in horses:
        print(x)
    input("")