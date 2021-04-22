import scipy.io.wavfile as sci
import wave
import numpy as np

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

wave = wave.open("/home/kir/and another one/hw_oip/python/SOUND.wav")
sound = sci.read("/home/kir/and another one/hw_oip/python/SOUND.wav")

print(len(sound[1]) / sound[0] // 60, "m" ,(len(sound[1] / sound[0]) % 60), "s")
print("n =", sound[0], "Hz")
print(type(sound[1][0][0]))
print("nchannels =", wave.getnchannels())

a = np.array(sound[1])
a = a[:, 0]
print(max(a), min(a))