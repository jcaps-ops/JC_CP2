import csv
import time
def fancy_print(count,line):
    print(f"{count},Title:{line[0]} --- Year:{line[4]} --- Genres:{line[2]}")
    print(f"    director:{line[3]} --- Actors:{line[4]} --- Length:{line[5]}")
def main():
    catagories = []
    while True:
        ply_answer = input("What do you want to do (1,Show movie list)")
        if ply_answer == "1":
            return "1",catagories
        if ply_answer == "2":
            search = input("search by (1.Genre 6.Search)")
            if search == "1":
                cat_add = input("What Genre")
                catagories.append(cat_add.capitalize())
            if search == "6":
                return "2",catagories
                
    # to make a search list of catagores to search for
with open('Indvival_projects\Movies list - Sheet1.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  player_action = main()
  if player_action[0] == "1":
    count = 0
    for lines in csvFile:
        count += 1
        fancy_print(count,lines)
        time.sleep(0.1)
  if player_action[0] == "2":
      for w in player_action[1]:
        print(w)
        for lines in csvFile:
            for x in lines:
                for y in player_action[1]:
                    x = x.split("/")
                    if y in x:
                        print(lines)
                        time.sleep(0.1)
