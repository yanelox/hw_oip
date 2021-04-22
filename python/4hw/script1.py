import inglib as kl
import RPi.GPIO as GPIO

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

kl.start()

com = 17
GPIO.setup(com, GPIO.OUT)

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

val = 0
GPIO.output(com, 1)

while val != -1:
    print ("Enter value(-1 to exit):\n")

    val = kl.getValue()

    if val == -1:
        break

    kl.num2dac(val, 1)

    print(val, "=", kl.getVoltage(val), "V\n")

GPIO.output(com, 0)
kl.num2dac(0, 1)