#JC class notes

class worker:
    #the varibles you need
    def __init__(self, name, clas, aged):
        self.name = name.capitalize()
        self.clas = clas.capitalize()
        self.aged = aged
    def __str__(self):
        return f"Name of id 001:{self.name}\n Class:{self.clas}\n Age:{self.aged}"
    
    def speak(self):
        return f'{self.name}: I love my Corparate overlords!'




doug = worker("Doug", "Lower class", 23)
willhelm = worker("willhelm", "upper class", 19)
print(willhelm)
print(doug)
print(doug.speak())
print(doug.speak())
print(doug.speak())
