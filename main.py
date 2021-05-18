import numpy as np
import math 
numbers=""
sorted1=[]
current=0
floored=0
ceiling=0
numbers = input("array of numbers ")
numbers = numbers.split()
sorted1 = [int(numeric_string) for numeric_string in numbers]
sorted2 = np.sort(sorted1)
total=0
finalmedian=0
print(" ")
print(sorted2)
print(" ")
for i in sorted2:
        current = current + i
finalmode = current/len(numbers)
print("MEAN: " + str(finalmode))
print(" ")
if np.bincount(sorted2).argmax() > sorted2[0]:
        print("MODE: "+str(np.bincount(sorted2).argmax()))
else:
        print("MODE: N/A or 1")
length1 = len(sorted2)
print(" ")
length2 = length1 - 1
if (length1 % 2) == 0: 
        length2 = length2/2
        floored = math.floor(length2) 
        ceiling = math.ceil(length2)
        total = sorted2[floored] + sorted2[ceiling]
        finalmedian = total/2
        print("MEDIAN: " + str(finalmedian))
        
        
else:
        median = str(sorted2[length1/2])
        print("MEDIAN:"+ str(median))
print(" ")
# Python program to find difference between two numbers

# first number
num1 = sorted2[0]
# second number
num2 = sorted2[len(sorted2)-1]

# num1 is greater than num2
if num1 > num2:
    diff = num1 - num2
# num1 is less than num2
else:
    diff = num2 - num1

# print difference value
print('RANGE: ', diff)
print(" ")
print('LARGEST: ', num2)
print(' ')
print('SMALLEST: ', num1)