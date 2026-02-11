#Jhc 2nd expanded persoanl libary
import csv

def Libary_writer(action):

        if action == 1:
            readfill(1)
        if action == 2:
            readfill(2)   
        if action == 3:
           libary = readfill(3)
           with open("Indvival_projects\Libary.csv", "w", newline = "") as csvfile:
            fieldnames = ["Title","Creator","Year","Genre"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvfile.truncate(0)
        if action == 4:
            readfill(4)

def readfill(action):
     with open("Indvival_projects\Libary.csv", "r+", newline = "") as csvfile:
                if action == 1:
                    libary = []
                    for line in csvfile:
                        libary.append(line.strip())
                    return libary
                if action == 2:
                    fieldnames = ["Title","Creator","Year","Genre"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    Book_name = input("What book do you want to add to the libary:")
                    #Asks for the author of the book
                    Book_author = input("What is the authors name:")
                    Book_year = input("What is the year the book was made:")
                    Book_genre = input("What is the genre of the book:")
                    addition = {"Title":Book_name,"Creator":Book_author,"Year":Book_year,"Genre":Book_genre}
                    #writer.writerow(fieldnames)
                    writer.writerow(addition)
                if action == 3:
                    libary = []
                    for line in csvfile:
                        libary.append(line.strip())
                        print(libary)
                    return(libary)
                if action == 4:
                    for line in csvfile:
                        print(line)
                if action == 5:
                    for line in csvfile:
                        print(line)
                


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




#Function for add to the liabry 
def Add_too(libary):
    #Asks for the name of the book
    Book_name = input("What book do you want to add to the libary:")
     #Asks for the author of the book
    Book_author = input("What is the authors name:")
     #Just adds it
    Libary_writer(2)

    return libary
#Function for add to the liabry 
def veiw_lib(libary):
    #Add to a counter for the looks 
    counter = 0
    #Itertating over it so i can display the options
    for key, value in libary.items():
        #Bigger number
        counter += 1
        #Show it
        print(f"{counter},{key}:{value}")

def menu(libary):
    #Start a while loo[]
    playering = True
    while playering:
        #Asks them it
        print("What option do you want to do 1.Add to your libary 2.Show your libary 3.Remove a book from the libary 4.Search for a book 5.exit")
        #Just send them to the right functiomn
        answer = playerchecker(5)
        if answer == 1:
            Libary_writer(2)
        if answer == 2:
            Libary_writer(4)
        if answer == 3:
            Libary_writer(3)
        if answer == 4:
            search(libary)
        if answer == 5:
            playering = False

def remove(libary):
    #Ask them for which option to remove
    Book_name = input("What book do you want to remove from the libary:")
    libary.pop(Book_name)
    return libary
def search(libary):
    #Ask them for which option to search via
    print("Do you want to search via 1.Book name or 2.Author")
    option = playerchecker(2)
    #Were just going to use the .get to find the option
    if option == 1:
        Book_name = input("What book are you looking for ")
        if Book_name in libary:
            book_author = libary.get(Book_name)
            print(f"{Book_name}:{book_author}")
    if option == 2:
        #Iterates it over til lwe found the proper answer
        book_author = input("What Author are you looking for ")
        Book_name = []
        for x in libary:
                test = libary.get(x)
                if test == book_author:
                    Book_name.append(x)
        #Then just print it
        print(f"{Book_name} was written by {book_author}")




libary = Libary_writer(1)
menu(libary)
