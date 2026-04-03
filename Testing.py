# Import libraries
import matplotlib.pyplot
import numpy as np

def piegraph(inputexpences,InputCats):
        fig = matplotlib.pyplot.figure(figsize=(10, 8))
        matplotlib.pyplot.pie(inputexpences, labels=InputCats)

        # show plot
        matplotlib.pyplot.show()
def bargraph(Categories, expences):
        matplotlib.pyplot.bar(Categories, expences)
        matplotlib.pyplot.title('Expenses per categories')
        matplotlib.pyplot.xlabel('Catagories')
        matplotlib.pyplot.ylabel('Expences')
        matplotlib.pyplot.show()

#bargraph(['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES'],[23, 17, 35, 29, 12, 41])
#PieChart([])
piegraph([100,150,200,700],["food","emergencies","water","rent"])