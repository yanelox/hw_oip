# import RPi.GPIO as GPIO
import time 

def start(mode):
    GPIO.setmode (GPIO.BCM)

    pins = 0

    if mode == 0:
        pins = [24, 25, 8, 7, 12, 16, 20, 21] #LED
    elif mode == 1:
        pins = [10, 9, 11, 5, 6, 13, 19, 26] #DAC

    GPIO.setup (pins, GPIO.OUT)

    return pins

def lightUp (ledNumber, period):
    pin = pins[ledNumber]

    GPIO.output (pin, 1)

    time.sleep (period)

    GPIO.output (pin, 0)


def blink (ledNumber, blinkCount, blinkPeriod):
    pin = pins[ledNumber]

    for i in range (blinkCount):
        lightUp (ledNumber, blinkPeriod)

        time.sleep (blinkPeriod)

    GPIO.output (pins, 0)

def runningLight (count, period):
    for i in range (count):
        for j in range(8):
            lightUp (j, period)

def runningDark (count, period):
    GPIO.output (pins, 1)

    for i in range (count):
        for j in range(8):
            GPIO.output (pins[j], 0)

            time.sleep (period)

            GPIO.output (pins[j], 1)

    GPIO.output (pins, 0)


def decToBinList (decNumber):
    res = [0 for i in range (8)]

    for i in range (8):
        res[7-i] = decNumber % 2

        decNumber = decNumber // 2

    return res

def lightNumber (number):
    decNumber = decToBinList (number)
    decNumber = decNumber [::-1]

    GPIO.output (pins, decNumber)


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

def runningPattern (pattern, direction):
    for i in range (9):
        print (decToBinList (pattern))
        GPIO.output (pins, decToBinList(pattern)[::-1])

        time.sleep (1)
        
        pattern = numberShift (pattern, direction)

    GPIO.output (pins, 0)

def lightUpPWM (ledNumber):
    p = GPIO.PWM (pins[ledNumber], 100)
    p.start (0)

    for i in range (0, 100, 5):
        p.ChangeDutyCycle (i)
        time.sleep (0.1)

    for i in range (100, 0, -5):
        p.ChangeDutyCycle (i)
        time.sleep (0.1)

    p.stop()

def num2dac(value):
    lightNumber(value)

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

    num2dac(0)

    while GPIO.input(pin) != 1 and val < 256:
        val += 1
        num2dac (val)

    return val

def binSearch(pin):
    max_val = 255
    min_val = 0

    val = max_val // 2

    num2dac(val)

    for i in range(8):
        if GPIO.input(pin) == 1:
            val = (val + min_val) // 2

        else:
            val = (val + max_val) // 2

        num2dac(val)

    return val

def getLevel(value):
    res = 0
    interval = 255 // 9 + 1

    tmp = value // interval

    for i in range(tmp):
        res += 2 ** (7 - i)

    return res

def setLevel(value):
    lightNumber (getLevel(value))