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
                target_rand = random.randrange(0,len(Enemeies))
                target = Enemeies[target_rand]
                target[1] = target[1] - dam
                print(f"{x[0]} used \n{cards_used[0]},{cards_used[1]},{cards_used[2]}\n Dealing {dam} to {target[0]} leaving them with {target[1]} hp")
                input("")
        if len(Enemeies) > 0:
            print(len(Enemeies))
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
                target_rand = random.randrange(0,len(Troops))
                target = Troops[target_rand]
                target[1] = target[1] - dam
                print(f"{x[0]} used \n{cards_used[0]},{cards_used[1]},{cards_used[2]}\n Dealing {dam} to {target[0]} leaving them with {target[1]} hp")
                input("")

#Troop example ["Name", "Health","Tokens=[]","Strength","Cards = []","Return values"]
cards1 = ["Basic","Basic","Basic","Basic","Fire blaze"]
Troops = [["Greg", 20, [], 1,cards1,[]]]
enemies = [["creature", 10, [], 1,cards1],["creature", 10, [], 1,cards1]]

combat(Troops,enemies)