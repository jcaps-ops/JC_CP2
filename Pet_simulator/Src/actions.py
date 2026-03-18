
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
        self,living = living
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
        
        
        return f"================\n================\nName:{self.name}\nspecies:{self.species}\nage:{self.age}\nhunger:{hunger_dis} {self.hunger * 10}%\nhappy levels:{happiness_dis} {self.happiness * 10}%\nEnergy:{energy_dis} {self.energy * 10}%"
    
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
            print("your pet has died")
        if self.energy <= 0:
            self.living = False
            print("your pet has died")
        if self.age >= self.lifespan:
            self.living = False
            print("your pet has died from old age")
    
    def play(self):
        answering = True
        while answering == True:
            ply_imp = input("What option do you want(1-3)")


        

    

doug = creature("Doug","Human",23,8,10,10)
print(doug.stat_screen())

