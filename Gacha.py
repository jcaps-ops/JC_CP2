import random

def card_draw(cards,Strength):
    damage = 0
    card_len = len(cards)
    cards_used = []
    for x in range(0,3):
        randcard = random.randrange(0,card_len)
        y = cards[randcard]
        if y == "Basic":
            damage += Strength
            cards_used.append(y)
        if y == "Fire blaze":
            damage += 5
            damage += Strength
            cards_used.append(y)
        if y == "Fire dance":
            Strength += 1
            cards_used.append(y)
    return cards,damage,Strength,cards_used

def combat(Troops,Enemeies):
    while True:
        if len(Troops) > 0:

            for x in Troops:
                if x[1] <= 0:
                    Troops.pop(Troops.index(x))
                    continue
                dam = 0
                cards_used = []
                card_draw_var = card_draw(x[4],x[3])
                x[4] = card_draw_var[0]
                dam = card_draw_var[1]
                x[3] = card_draw_var[2]
                cards_used = card_draw_var[3]
                if len(Enemeies) > 0:
                    target_rand = random.randrange(0,len(Enemeies))
                    target = Enemeies[target_rand]
                    target[1] = target[1] - dam
                    print(f"{x[0]} used \n{cards_used[0]},{cards_used[1]},{cards_used[2]}\n Dealing {dam} to {target[0]} leaving them with {target[1]} hp")
                    input("")
        else:
            return Troops,Enemeies
        if len(Enemeies) > 0:
            for x in Enemeies:
                if x[1] <= 0:
                    Enemeies.pop(Enemeies.index(x))
                    continue
                dam = 0
                cards_used = []
                card_draw_var = card_draw(x[4],x[3])
                x[4] = card_draw_var[0]
                dam = card_draw_var[1]
                x[3] = card_draw_var[2]
                cards_used = card_draw_var[3]
                if len(Troops) > 0:
                    target_rand = random.randrange(0,len(Troops))
                    target = Troops[target_rand]
                    target[1] = target[1] - dam
                    print(f"{x[0]} used \n{cards_used[0]},{cards_used[1]},{cards_used[2]}\n Dealing {dam} to {target[0]} leaving them with {target[1]} hp")
                    input("")
        else:
            return Troops,Enemeies
#Troop example ["Name", "Health","Tokens=[]","Strength","Cards = []","Return values"]
cards1 = ["Fire dance","Fire dance","Basic","Basic","Fire blaze","Fire blaze"]
cards2 = ["Basic","Basic","Basic"] 
Troops = [["Greg", 20, [], 1,cards1,[]]]
enemies = [["creature", 10, [], 1,cards2],["creature", 10, [], 1,cards2]]
while True:
    combat(Troops,enemies)
    print("WAVE DONE")
    enemies = [["creature", 10, [], 1,cards2],["creature", 10, [], 1,cards2]]

    if Troops == []:
        break