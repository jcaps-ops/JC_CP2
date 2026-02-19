def word_counter(Good_friday):
    try:
        with open(Good_friday, "r", newline = "") as document:
            for line in document:

                print(line)
    except:
        print("That file does not work")
def add(Good_friday):
    try:
        with open(Good_friday, "a", newline = "") as document:
            print("test")
    except:
        print("That file does not work")

ply_int = input("What file do you want to use")
word_counter(ply_int)
