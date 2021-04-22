import scipy.io.wavfile as sci
import RPi.GPIO as GPIO
import wave
import numpy as np
import inglib as kl
import time

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

kl.start()

wave = wave.open("/home/student/tmp/hw_oip/python/SOUND.wav")
sound = sci.read("/home/student/tmp/hw_oip/python/SOUND.wav")

# print(len(sound[1]) / sound[0] // 60, "m" ,(len(sound[1] / sound[0]) % 60), "s")
# print("n =", sound[0], "Hz")
# print(type(sound[1][0][0]))
# print("nchannels =", wave.getnchannels())

a = np.array(sound[1])
a = np.float64(a[:, 0])


a = (a + 32768) / 65536 * 255
a = list(map(int, a))

for i in a:
    kl.num2dac(i, 1)
    for j in range(6):
        time.sleep(0)