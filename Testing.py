# Import libraries
import matplotlib
import numpy as np


# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']

data = [23, 17, 35, 29, 12, 41]

# Creating plot
fig = matplotlib.pyplot.figure(figsize=(10, 8))
matplotlib.pyplot.pie(data, labels=cars)

# show plot
matplotlib.pyplot.show()