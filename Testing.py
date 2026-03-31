# Import libraries
import matplotlib.pyplot
import numpy as np

def piechart():
        # Creating dataset
        cars = ['AUDI', 'BMW', 'FORD',
                'TESLA', 'JAGUAR', 'MERCEDES']

        data = [23, 17, 35, 29, 12, 41]

        # Creating plot
        fig = matplotlib.pyplot.figure(figsize=(10, 8))
        matplotlib.pyplot.pie(data, labels=cars)

        # show plot
        matplotlib.pyplot.show()
def bargraph(Categories, expences):
        matplotlib.pyplot.bar(Categories, expences)
        matplotlib.pyplot.title('Expenses per categories')
        matplotlib.pyplot.xlabel('Catagories')
        matplotlib.pyplot.ylabel('Expences')
        matplotlib.pyplot.show()

#bargraph(['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES'],[23, 17, 35, 29, 12, 41])
