
#This function prints out all that we need to see Yippe by just looping over the document 
def word_counter(Good_friday):
    try:
        with open(Good_friday, "r", newline = "") as document:
            doc = []
            for x in document:
                print(x)
                doc += x
            return(doc)
    except:
        print("That file does not work")
#This functions add lines to the document by just appeneding them to the document and the time and word count
#Future jaxon here after i coded this I DESPISE THIS SECTION JUST STRIKE ME DOWN PLEASE
def add(Good_friday,doc,time,word_count):
    try:
        with open(Good_friday, "a", newline = "") as document:
            answering = True
            while answering:
                doc_true = input("What line would you like to add(to exit type):")
                if doc_true == "exit":
                    answering = False
                else:
                    document.write(doc_true)
                    document.write("\n")
                    

            document.write(f"The time last date is {time[0]} The last acess time is {time[1]}\n")
            document.write(f"The word count is {word_count}\n")
    except:
        print("That file does not work")

#This one is just to get the word count we need
def word_counts(Good_friday):
    try:
        count = 0
        with open(Good_friday, "r", newline = "") as document:
            data = document.read()
            words = data.split()
            count += len(words)
            return(count)
    except:
        print("That file does not work")

