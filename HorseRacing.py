import random
def race(horses):
    racing = True
    while racing == True:
        for x in horses:
            pass


def raceturn(horse):
    if horse[2] > 0:
        for x in horse[2]:
            horse[3] = horse[3] + random.randrange(1,horse[1])
        horse[2] = horse[2] - 1
    else:
        horse[2] = horse[4]


#Example horse [Name,Speed,stanmina,meter,maxstamina,wins,loses]