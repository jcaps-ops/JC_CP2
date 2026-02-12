#JCH 2nd person libary expanded
import csv
with open("Indvival_projects/libary.csv", "w") as csvfile:
    fieldnames = ["Title","Author","Year","Genre"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    booktitle = input("Book Name:")
    bookName = input("Author Name:")
    bookYear = input("Year Name:")
    bookGenre = input("Genre Name:")
    libary = []
    for lines in csvfile:
        libary.append(lines)
    libary.append({"Title":booktitle,"Author":bookName,"Year":bookYear,"Genre":bookGenre})
    writer.writerows(libary)