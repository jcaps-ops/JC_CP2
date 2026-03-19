def Storage():
    with open("Pet_simulator\Documentation\pet_info.csv", "a", newline = "") as csvfile:
        fieldnames = ["self", "name", "species", "age", "hunger","happiness","energy","timer","days","living","lifespan"]
        writer = csvfile.write(csvfile)

        #writer.writerow(fieldnames)
        writer.writerow({"Doug","Human","23","8","10","10","0","0","True","24"})

Storage()
