import random 
import time
from faker import Faker
fake = Faker()


hype = 0
chaters = []
def generate_chaters(chaters):
    list = []
    for x in range (0,chaters):
        fakername = fake.domain_word()
        list.append(fakername)
        print(f"{fakername} has joined the chat.")
        time.sleep((random.randrange(1, 10))/10)
    return list
def randomchat(chaters):
    random_chater = random.randrange(0,len(chaters))
    random_chater = chaters[random_chater]
    random_message = random.randrange(0,10)
    print(f"{random_chater}: {random_message}")

def chattick(hype,chaters):
    time.sleep(0.2)
    random_Chat_num = random.randrange(0,hype)
    for x in random_Chat_num:
        print()
def chat(hype):
    pass
        
chaters = generate_chaters(10)