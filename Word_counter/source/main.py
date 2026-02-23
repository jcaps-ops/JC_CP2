from file_reader import word_counter,add
from time_tracker import get_time

def main():
    while True:
        print("--- Word counter ---")
        print("1.Set the document")
        print("2.view the document")
        print("3.Add to the document")
        print("4.Exit")
        ply_imp = input("please imput(1-4):")
        if ply_imp == "1":
            ply_int = input("What file do you want to use:")
        elif ply_imp == "2":
            doc = word_counter(ply_int)
        elif ply_imp == "3":
            doc = word_counter(ply_int)
            time = get_time()
            add(ply_int,doc,time)
        elif ply_imp == "4":
            break
        else:
            print("that is not an option")
        

main()
    
