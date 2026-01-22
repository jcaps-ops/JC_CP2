#Jc 2nd password generator
import string
import random

def playerchecker(options):
    #Check if the players input is good
    works = True
    while works:
        ply_input = input("Enter here:")
        if ply_input.isnumeric() == True:
            ply_input = int(ply_input)
            works = False
            if options != 0:
                if ply_input <= options:
                    works = False
                else:
                    works = True
    return ply_input    

def pass_gen(req):
    print("How long do you want your password")
    leng = playerchecker(0)
    #Based on if it is in the requirments then randomly generate a password for it
    req_len = len(req)
    string_an = ""
    for x in range(0,leng):
        #Generates a random thing from the list
        req_ran = req[random.randrange(0,req_len)]
        #Then will generate a random one form this list
        if req_ran == "Low":
            ran = random.randrange(97,122)
        if req_ran == "Up":
            ran = random.randrange(65,90)
        if req_ran == "num":
            ran = random.randrange(48,57)
        if req_ran == "char":
            ran = random.randrange(33,47)
        ran = chr(ran)
        string_an = string_an + ran
    print(f"This is your new password {string_an}")
    print("Do you want to generate another password 1.Yes 2.No")
    con = playerchecker(2)
    if con == 1:
        mainmenu()
#A function that despays and get what they want to add
def mainmenu():
    #Creats varablies needed 
    end = False
    Requirements = []
    working = True
    #Creats a loop 
    while working == True:
        #Just this asking questions then adding to a list so i know what to be able to generate 
        print("Should it have lowercases 1.Yes 2.No")
        answer = playerchecker(2)
        if answer == True:
            Requirements.append("Low")
            end = True
        print("Should it have Uppercases 1.Yes 2.No")
        answer = playerchecker(2)
        if answer == True:
            Requirements.append("Up")
            end = True
        print("Should it have Numbers 1.Yes 2.No")
        answer = playerchecker(2)
        if answer == True:
            Requirements.append("num")
            end = True
        print("Should it have Special charaters 1.Yes 2.No")
        answer = playerchecker(2)
        if answer == True:
            Requirements.append("char")
            end = True
        if end == True:
            working = False
    pass_gen(Requirements)
#test = [{"sword",{"Requirement","None","Stat","strenght of 2"}}]

mainmenu()