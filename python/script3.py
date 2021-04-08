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

X = np.arange(0, time, 1 / samplingFrequency)

ndarray = list(map(int, 127.5 * (np.sin(2 * np.pi * X * frequency) + 1)))

plt.figure(figsize = (13, 13))

plt.plot(X, ndarray)

plt.savefig("/home/kir/and another one/hw_oip/python/graph.png")