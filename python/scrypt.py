import RPi.GPIO as GPIO
import time 

GPIO.setmode (GPIO.BCM)
pins = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setup (pins, GPIO.OUT)

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
        res[7 - i] = decNumber % 2

        decNumber = decNumber // 2

    return res

def lightNumber (number):
    decNumber = decToBinList (number)
    decNumber = decNumber [::-1]

    GPIO.output (pins, decNumber)

    time.sleep (1)

    GPIO.output (pins, 0)

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

# lightUp (4, 2)
# time.sleep (1)
# blink (2, 3, 1)
# time.sleep (1)
# runningLight (2, 0.2)
# time.sleep (1)
# runningDark (2, 0.2)
# time.sleep (1)
# print (decToBinList (3))
# lightNumber (3)
# time.sleep (1)
# runningPattern (5, 0)
# time.sleep (1)
lightUpPWM (3)
GPIO.cleanup()