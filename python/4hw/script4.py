import inglib as kl

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

pins = kl.start(0)

com = 

GPIO.setmode(com, GPIO.OUT)

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

val = 0
prev_val = 0

while True:
    val = kl.binSearch(com)

    if val != prev_val:
        kl.setLevel (val)

    prev_val = val