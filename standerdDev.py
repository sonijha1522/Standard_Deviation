import  numpy as np
import math
inputValue = [6, 2, 3, 1]
len1 = len(inputValue)

sum = 0
sum1 = 0
for counter in range(0, len1):
    sum = sum + inputValue[counter]
mean = (sum/len1)
print(" The mean value of inputvalue====", mean)
for counter1 in range(0, len1):
   sum1 = sum1 + (inputValue[counter1] -mean)**2
print( "sumation value====", sum1)

SD = math.sqrt(sum1/len1)
print("The standard deviation====", SD)



