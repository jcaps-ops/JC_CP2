import csv

'''try:
    with open("Notes/sample.txt", "r") as file:
        content = []
        for line in file:
            content.append(line.strip())
except:
    print("Can not find that file")
else:
    for line in content:
        print(line)
'''
try:
    with open("Notes/Class CSV sample - Sheet1.csv", mode= "r") as sample:
        reader = csv.reader(sample)
        for line in reader():
            print(line)
except:
    print("Can not find that file")
else:
    print("run ended")