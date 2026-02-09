import csv


"""
with open("Notes/Class CSV tester - Sheet1.csv", "w", newline = "") as csvfile:
    fieldnames = ["Username","Favorite color"]
    writer = csv.writer(csvfile)

    #writer.writerow(fieldnames)
    writer.writerow({"zen_guy", "white"})
    writer.writerow({"sky_faller", "sky blue"})
"""
"""
content = []
with open("Notes\sample.txt", "r+") as file:
    for line in file:
        content.append(line.strip())
    
    index = content.index("generation")
    content[index] = "family"

    file.truncate(0)

    for name in content:
        file.write(name + "\n")

print("code Ends")
"""
users = [{"Username":"retro_gamer","Favorite color":"coral"},{"Username":"zen_master","Favorite color":"coral"},]
with open("Notes/Class CSV tester - Sheet1.csv", "r+", newline = "") as csvfile:
    fieldnames = ["Username","Favorite color"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writerow(fieldnames)
    writer.writerows(users)
