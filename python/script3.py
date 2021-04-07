import numpy as np
import matplotlib.pyplot as plt

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def getFloatValue():
    res = -42

    while res < 0:
        try:
            res = float(input())

        except:
            print("Incorrect input")

    return res

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

print("Введите 3 числа (time, frequency, samplingFrequency)")

time = getFloatValue()
frequency = getFloatValue()
samplingFrequency = getFloatValue()

ndarray = np.arange (0, time, 1 / samplingFrequency)

Y = np.sin (ndarray)

plt.figure (figsize = (13, 13))

plt.plot (ndarray, Y)

plt.savefig ("/home/kir/and another one/hw_oip/python/graph.png")