import numpy as np
import script1 as sc1

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def getValue():
    res = -42
    
    while res < 0:
        try:
            res = int(input())

        except:
            print("Incorrect input")

    return res

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

print ("Введите число повторений")

repetitionsNumber = getValue()

for i in range(repetitionsNumber):
    for j in range(256):
        sc1.num2dac(j)

    for j in range(256):
        sc1.num2dac(256 - j)