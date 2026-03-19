import random
class creature:
    def __init__(self, name, species, age, hunger,happiness,energy,timer,days,living,lifespan):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.timer = timer
        self.days = days
        self.living = living
        self.lifespan = lifespan

    def stat_screen(self):
        hunger_dis_list = []
        happy_dis_list = []
        energy_dis_list = []
        for x in range(0,self.hunger):
            hunger_dis_list.append("█")
        for x in range(0,10-self.hunger):
            hunger_dis_list.append("░")
        hunger_dis = ""
        for y in range(0,len(hunger_dis_list)):
            hunger_dis = hunger_dis + hunger_dis_list[y]
        
        for x in range(0,self.happiness):
            happy_dis_list.append("█")
        for x in range(0,10-self.happiness):
            happy_dis_list.append("░")
        happiness_dis = ""
        for y in range(0,len(happy_dis_list)):
            happiness_dis = happiness_dis + happy_dis_list[y]
        
        for x in range(0,self.energy):
            energy_dis_list.append("█")
        for x in range(0,10-self.energy):
            energy_dis_list.append("░")
        energy_dis = ""
        for y in range(0,len(energy_dis_list)):
            energy_dis = energy_dis + energy_dis_list[y]
        
        
        return f"================\n================\nName:{self.name}\nspecies:{self.species}\nage:{self.age}\nDay:{self.days}\nHour:{self.timer}\nhunger:{hunger_dis} {self.hunger * 10}%\nhappy levels:{happiness_dis} {self.happiness * 10}%\nEnergy:{energy_dis} {self.energy * 10}%"
    
    def day_cycle(self):
        if self.timer >= 24:
            self.days += 1
            self.timer = self.timer - 24
            self.hunger -= 1
            self.energy -= 2
            self.happiness -= 1
        if self.days == 30:
            self.age += 1
            self.days = 0

    def death(self):
        if self.happiness <= 0:
            self.hunger -= 2
            self.energy -= 2
        if self.hunger <= 0:
            self.living = False
            print("your Creature has died")
        if self.energy <= 0:
            self.living = False
            print("your Creature has died")
        if self.age >= self.lifespan:
            self.living = False
            print("your Creature has died from old age")
    
    def play(self,Activity):
        answering = True
        print("Do you want to 1:play fetch with the creature")
        print("Do you want to 2:Hunt with your creature")
        print("Do you want to 3:Hunt your creature")
        print("Do you want to 4:Exit")
        while answering == True:
            ply_imp = input("What option do you want(1-4)")
            Activity = ply_imp
            if Activity == "1":
                print("you played with your little creature")
                print("Your Creature lost 2 energy:")
                self.energy -= 2
                print("Your Creature gained 2 happiness")
                self.happiness += 2
                print("1 hour has passed")
                self.timer += 1
                answering = False
            elif Activity == "2":
                print("you hunted with your little creature")
                print("Your Creature lost 4 energy:")
                self.energy -= 4
                print("Your Creature gained 1 happiness")
                self.happiness += 1
                print("Your Creature gained 1 hunger")
                self.hunger += 1
                print("4 hours has passed")
                self.timer += 4
                answering = False
            elif Activity == "3":
                print("you hunted your little creature")
                print("Your Creature lost 4 energy:")
                self.energy -= 4
                print("Your Creature lost 1 happiness")
                self.happiness -= 1
                print("2 hours has passed")
                self.timer += 2
                answering = False
            elif Activity == "4":
                answering = False
            else:
                print("That is not an option")
        self.day_cycle()
        self.death()
        self.regulations()

    def eat(self,Activity):
        answering = True
        print("Do you want to feed your creature 1:Creature kibble")
        print("Do you want to feed your creature 2:Fresh meat")
        print("Do you want to feed your creature 3:Dessert")
        print("Do you want to 4:Exit")
        while answering == True:
            ply_imp = input("What option do you want(1-4)")
            Activity = ply_imp
            if Activity == "1":
                print("Your Creature gained 3 food")
                self.hunger += 3
                print("Your Creature lost 1 happiness")
                self.happiness += 1
                print("1 hour has passed")
                self.timer += 1
                answering = False
            elif Activity == "2":
                print("Your Creature gained 1 happiness")
                self.happiness += 1
                print("Your Creature gained 1 hunger")
                self.hunger += 1
                print("4 hours has passed")
                self.timer += 4
                answering = False
            elif Activity == "3":
                print("Your Creature lost 2 energy:")
                self.energy -= 2
                print("Your Creature gained 2 happiness")
                self.happiness += 2
                print("Your Creature gained 1 hunger")
                self.hunger += 1
                print("2 hours has passed")
                self.timer += 2
                answering = False
            elif Activity == "4":
                answering = False
            else:
                print("That is not an option")
        self.day_cycle()
        self.death()
        self.regulations()

    def regulations(self):
        if self.energy > 10:
            self.energy = 10
        if self.hunger > 10:
            self.hunger = 10
        if self.happiness > 10:
            self.happiness = 10

    def sleep(self):
        rand_slep = random.randrange(4,12)
        print(f"Your Creature sleept for {rand_slep * 3} hours")
        print(f"Your Creature gained {rand_slep} energy")
        self.hunger -= 2
        self.timer += rand_slep * 3
        self.day_cycle()
        self.death()
        self.regulations()

def main_menu():
    answer = True
    while answer == True:
        ply_repon = input(f"[1] Feed Pet\n[2] Play with Pet\n[3] Put Pet to Sleep\n[4] Check Status\n[5] Pet Management\n[6] Save Game\n[7] Load Game\n[8] Quit\n Which option:")
        if ply_repon == "1":
            doug.eat(1)
        elif ply_repon == "2":
            doug.play(1)
        elif ply_repon == "3":
            doug.sleep()
            input("")
        elif ply_repon == "4":
            print(doug.stat_screen())
            input("")
        
        

doug = creature("Doug","Human",23,8,10,10,0,0,True,24)
main_menu()



