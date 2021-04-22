import inglib as kl
import RPi.GPIO as GPIO
import time

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

kl.start()

pot = 17
com = 4

GPIO.setup(pot, GPIO.OUT)
GPIO.setup(com, GPIO.IN)

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

val = 0
prev_val = 0
GPIO.output(pot, 1)

while True:
    val = kl.binSearch (com)

    if val != prev_val:
        print("Digital value: ", val, "\nAnalog value: ", kl.getVoltage(val), " Vi\n")
    
    prev_val = val

GPIO.output(pot, 0)
kl.num2dac(0, 1)