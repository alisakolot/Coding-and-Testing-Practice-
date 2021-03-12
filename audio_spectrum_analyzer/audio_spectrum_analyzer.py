import pyaudio
import struct 
# unpack audio data into integers

import numpy as np 
import matplotlib.pyplot as plt 


# will display different window
# %matplotlib tk 

CHUNK = 1024 * 4 
# how much audio will be processed at a time
FORMAT = pyaudio.paInt16
# Bytes per sample
CHANNELS = 1 
# One mic, one sound
RATE = 44100
# Samples per second, Kh

p = pyaudio.PyAudio()
# Create class instance, main pyaudio object 
stream = p.open(
    format=FORMAT, 
    channels = CHANNELS,
    rate = RATE, 
    input = True, 
    output = True,
    frames_per_buffer = CHUNK 
)
# stream object

data = stream.read(CHUNK)
# data object, when 'data' is run, you will get a bunch of bytes  
print(data)
print("\n *** Program ran *** \n")