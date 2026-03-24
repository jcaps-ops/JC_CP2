class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Non descript noise")

class car(Vehicle):
    pass

class boat(Vehicle):
    def move(self):
        print("Noise")

Car = car("Ford","mustang")
oat = boat("AH","Tourings 20")