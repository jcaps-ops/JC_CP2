#Jc 2nd personal libary


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



libary = {}

#Function for add to the liabry 
def Add_too(libary):
    #Asks for the name of the book
    Book_name = input("What book do you want to add to the libary:")
     #Asks for the author of the book
    Book_author = input("What is the authors name:")
     #Just adds it
    libary[Book_name] = Book_author

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

def menu():
    
