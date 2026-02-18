#Jhc 2nd expanded persoanl libary
import csv

def Libary_writer(action):

        if action == 1:
            add()
        if action == 2:
            readfill(2)   
        if action == 3:
           readfill(3)
        if action == 4:
            readfill(4)

def readfill(action):
     with open("Indvival_projects/Indvival_projects\Libary.csv", "r+", newline = "") as csvfile:
                if action == 2:
                    for line in csvfile:
                        print(line)
                if action == 3:
                    print("What do you want to search for 1.Name 2.Author:")
                    great_input = playerchecker(2)
                    if great_input == 1:
                        Book_name = input("What book do you want to remove from the libary:")
                    if great_input == 2:
                        book_author = input("What is the name of the author to remove from:")
                    libary = []
                    for line in csvfile:
                        line = line.split(",")
                        if great_input == 1:
                            cheker = str(line[0])
                            if Book_name == cheker:
                                pass
                            else:
                                line = {"Title":line[0],"Creator":line[1],"Year":line[2],"Genre":line[3]}
                                libary.append(line)
                        if great_input == 2:
                            cheker = str(line[1])
                            if book_author == cheker:
                                pass
                            else:
                                line = {"Title":line[0],"Creator":line[1],"Year":line[2],"Genre":line[3]}
                                libary.append(line)
                            
                    write(libary)
                    
                if action == 4:
                    print("What do you want to search for 1.Name 2.Author:")
                    great_input = playerchecker(2)
                    if great_input == 1:
                        Book_name = input("What book do you want to search for from the libary:")
                    if great_input == 2:
                        book_author = input("What is the name of the author to search for:")
                    libary = []
                    for line in csvfile:
                        line = line.split(",")
                        if great_input == 1:
                            cheker = str(line[0])
                            if Book_name == cheker:
                                print(f"Title:{line[0]},Creator:{line[1]},Year:{line[2]},Genre:{line[3]}")
                        if great_input == 2:
                            cheker = str(line[1])
                            if book_author == cheker:
                                print(f"Title:{line[0]},Creator:{line[1]},Year:{line[2]},Genre:{line[3]}")
                
                if action == 5:
                    for line in csvfile:
                        print(line)
                if action == 6:
                    Look_for_book = input("What is the name of the book your looking for")
                    for line in csvfile:
                        print(line)
                        print(line[0])
                        if line[0] == Look_for_book:
                            print(line)
def add():
    with open("Indvival_projects/Indvival_projects\Libary.csv", "a", newline = "") as csvfile:
        fieldnames = ["Title","Creator","Year",'Genre']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        Book_name = input("What book do you want to add to the libary:")
        #Asks for the author of the book
        Book_author = input("What is the authors name:")
        Book_year = input("What is the year the book was made:")
        Book_genre = input("What is the genre of the book:")
        #writer.writerow(fieldnames)
        writer.writerow({"Title":Book_name,"Creator":Book_author,"Year":Book_year,"Genre":Book_genre})

def write(Libary):
    with open("Indvival_projects/Indvival_projects\Libary.csv", "w", newline = "") as csvfile:
        fieldnames = ["Title","Creator","Year",'Genre']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(Libary)

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



def menu():
    #Start a while loo[]
    playering = True
    while playering:
        #Asks them it
        print("What option do you want to do 1.Add to your libary 2.Show your libary 3.Remove a book from the libary 4.Search for a book 5.exit")
        #Just send them to the right functiomn
        answer = playerchecker(5)
        if answer == 1:
            Libary_writer(1)
        if answer == 2:
            Libary_writer(2)
        if answer == 3:
            Libary_writer(3)
        if answer == 4:
            Libary_writer(4)
        if answer == 5:
            playering = False

menu()
