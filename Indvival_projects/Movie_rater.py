import csv
import time
#Just facy print
def fancy_print(count,line):
    print(f"{count},Title:{line[0]} --- Rating:{line[3]} --- Genres:{line[2]}")
    print(f"    director:{line[1]} --- Actors:{line[5]} --- Length:{line[4]}")
def main():
    #Catigories to seach from
    catagories = ["None","None","None","None","None"]
    while True:
        ply_answer = input("What do you want to do (1,Show full movie list 2.Search functions)")
        if ply_answer == "1":
            return "1",catagories
        
        if ply_answer == "2":
            searching = True
            while searching:
                #just having players slecting the option
                print(F"Catagories list:1, genres:{catagories[0]} 2, Actors:{catagories[1]}")
                print(F"Catagories list:3, Length:{catagories[2]} 4, Director:{catagories[3]}")
                search = input("search by (1.Genre 2,Actor 3,Length 4,Director 5,Clear search 6.Search 7,exit)")
                if search == "1":
                    #Ask for it then set it and capitlize it 
                    cat_add = input("What Genre")
                    catagories[0] = cat_add.capitalize()
                if search == "2":
                    #Ask for it then set it and capitlize it 
                    cat_add = input("What Actor")
                    cat_add = cat_add.split()
                    for x in cat_add:
                        cat_add[cat_add.index(x)] = x.capitalize()
                    cat_add =  " ".join(cat_add)
                    catagories[1] = cat_add
                if search == "3":
                    #Ask for it then set it and capitlize it 
                    answering = True
                    while answering:
                        cat_len = input("1,Less than 2,Greator than")
                        if cat_len == "1" or cat_len == "2":
                            catagories[4] = cat_len.capitalize()
                            answering = False
                    cat_add = input("What length of the movie")
                    catagories[2] = cat_add.capitalize()
                if search == "4":
                    #Ask for it then set it and capitlize it 
                    cat_add = input("What Diirector")
                    cat_add = cat_add.split()
                    for x in cat_add:
                        cat_add[cat_add.index(x)] = x.capitalize()
                    cat_add =  " ".join(cat_add)
                    catagories[3] = cat_add
                if search == "5":
                    #reset it all 
                    catagories = ["None","None","None","None","None"]
                if search == "6":
                    return "2",catagories
                if search == "7":
                    searching = False
                
    # to make a search list of catagores to search for
with open('Indvival_projects/Movies list - Sheet1.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  player_action = main()
  if player_action[0] == "1":
    count = 0
    for lines in csvFile:
        count += 1
        fancy_print(count,lines)
        time.sleep(0.1)
  if player_action[0] == "2":
      for lines in csvFile:
        for x in lines:
            for y in player_action[1]:
                x = x.split("/")
                if y in x:
                    print(lines)
                    time.sleep(0.1)