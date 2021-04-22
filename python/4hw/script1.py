import inglib as kl

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

pins = kl.start(1)

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

val = 0

while val != -1:
    print ("Enter value(-1 toe exit):\n")

    val = kl.getValue()

    kl.num2dac(val)

    print(val, " = ", kl.getVoltage(val), " V\n")