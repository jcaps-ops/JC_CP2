def word_counter(Good_friday):
    try:
        with open(Good_friday, "r", newline = "") as document:
            doc = []
            data = []
            ext_data = False
            for line in document:
                if ext_data == False:
                    if line != "-------":
                        doc.append(line)
                    else:
                        ext_data = True
                else:
                    data.append[line]
            for x in doc:
                print(x)
            for y in data:
                print(y)
            return(doc)
    except:
        print("That file does not work")
def add(Good_friday,doc,time):
    try:
        with open(Good_friday, "a", newline = "") as document:
            document.truncate(0)
            for x in doc:
                document.write(x)
            while True:
                doc_true = input("What line would you like to add(to exit type):")
                if doc_true == "exit":
                    break
                else:
                    document.write(doc_true)
            document.write("")
            document.write("-------")
            words = []
            for x in document:
                words.append(x.split)
            words_len = words.len()
            document.write(f"The word count is {words_len}")
            document.write(f"The last accesed data is {time[0]} the last accesed time was {time[1]}")

                    


    except:
        print("That file does not work")


