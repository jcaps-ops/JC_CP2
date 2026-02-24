"""
def factor(num):
    if num == 1: return 1 #< this is the base case that ends it

    return num * factor(num-1)
"""
"""
sequnce = [1,1]
number = 10
for i in range(1,number):
   sequnce.append(sequnce[i] + sequnce[i-1])

print(sequnce)
"""

"""
recursive_sequnce = [1,1]
def golden(n):
   if n == 1:
      return 0
   elif n == 2:
      return 1
   else:
      recursive_sequnce.append(recursive_sequnce[golden(n)] + recursive_sequnce)
"""

def fibinacci(n):
   if n == 1:
      return 1
   elif n == 2:
      return 1
   else:
       return fibinacci(n-1) + fibinacci(n-2)


print(fibinacci(10))