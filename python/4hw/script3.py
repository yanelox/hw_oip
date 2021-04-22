import inglib as kl

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

pins = kl.start(1)

com = #порт компаратора

GPIO.setmode(com, GPIO.OUT)

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

val = 0
prev_val = 0

while True:
    val = kl.binSearch (com)

    if val != prev_val:
        print("Digital value: ", val, "\nAnalog value: ", kl.getVoltage(val), " Vi\n")
    
    prev_val = val