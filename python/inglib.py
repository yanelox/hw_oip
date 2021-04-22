import RPi.GPIO as GPIO
import time 

pins = [[24, 25, 8, 7, 12, 16, 20, 21], [10, 9, 11, 5, 6, 13, 19, 26]] #LED, DAC

def start():
    GPIO.setmode (GPIO.BCM)

    GPIO.setup (pins[0], GPIO.OUT)
    GPIO.setup (pins[1], GPIO.OUT)


def lightUp (ledNumber, period, i):
    pin = pins[i][ledNumber]

    GPIO.output (pin, 1)

    time.sleep (period)

    GPIO.output (pin, 0)


def blink (ledNumber, blinkCount, blinkPeriod, i):
    pin = pins[i][ledNumber]

    for i in range (blinkCount):
        lightUp (ledNumber, blinkPeriod, i)

        time.sleep (blinkPeriod)

    GPIO.output (pins[i], 0)

def runningLight (count, period, i):
    for i in range (count):
        for j in range(8):
            lightUp (j, period, i)

def runningDark (count, period, k):
    GPIO.output (pins[k], 1)

    for i in range (count):
        for j in range(8):
            GPIO.output (pins[k][j], 0)

            time.sleep (period)

            GPIO.output (pins[k][j], 1)

    GPIO.output (pins[k], 0)


def decToBinList (decNumber):
    res = [0 for i in range (8)]

    for i in range (8):
        res[7-i] = decNumber % 2

        decNumber = decNumber // 2

    return res

def lightNumber (number, k):
    decNumber = decToBinList (number)
    decNumber = decNumber [::-1]

    GPIO.output (pins[k], decNumber)


def numberShift (number, direction):
    res= 0

    if direction == 0:
        tmp = (number // 128) % 2

        res = number << 1
        res += tmp
    
    elif direction == 1:
        tmp = number % 2
        
        res = number >> 1
        res = res + 128 * tmp

    res = res % 256

    return res

def runningPattern (pattern, direction, k):
    for i in range (9):
        print (decToBinList (pattern))
        GPIO.output (pins[k], decToBinList(pattern)[::-1])

        time.sleep (1)
        
        pattern = numberShift (pattern, direction)

    GPIO.output (pins, 0)

def lightUpPWM (ledNumber, k):
    p = GPIO.PWM (pins[k][ledNumber], 100)
    p.start (0)

    for i in range (0, 100, 5):
        p.ChangeDutyCycle (i)
        time.sleep (0.1)

    for i in range (100, 0, -5):
        p.ChangeDutyCycle (i)
        time.sleep (0.1)

    p.stop()

def num2dac(value, k):
    lightNumber(value, k)

def getValue():
    res = -42
    
    while res < -1:
        try:
            res = int(input())

            if res < -1:
                print("Incorrect input")
        
        except:
            print("Incorrect input")

    return res

def getVoltage(value):
    max_voltage = 3.3
    max_value = 255

    return value / max_value * max_voltage

def simpleSearch(pin):
    val = 0

    num2dac(0, 1)

    while GPIO.input(pin) == GPIO.HIGH and val < 256:
        val = val + 1
        num2dac (val, 1)
        time.sleep(0.001)

    num2dac(0, 1)

    return val

def binSearch(pin):
    r= 255
    l = 0

    num2dac((l + r) // 2, 1)
    time.sleep(0.001)

    for i in range(8):
        if GPIO.input(pin) == GPIO.LOW:
            r = (l + r) // 2

        else:
            l = (l +  r) // 2

        num2dac((l + r) // 2, 1)
        time.sleep(0.001)

    num2dac(0, 1)

    return (l + r) // 2

def getLevel(value):
    res = 0
    interval = 255 // 9 + 1

    tmp = value // interval

    for i in range(tmp):
        res += 2 ** (7 - i)

    return res

def setLevel(value, k):
    lightNumber (getLevel(value), k)