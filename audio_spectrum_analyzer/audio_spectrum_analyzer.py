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
# data object, when 'data' is run, you will get a bunch of bytes, but not integers  
    # can't plot in matplotlib, so you need to convert it 
    # [conversion using struct below]

data_int = struct.unpack(str(2 * CHUNK) + 'B',  data)
# print(len(data)) # length of data is double what our chunk is
# print(data_int)# a tuple, int vals 0=255
# this obj will give us integer data instead of byte data
# unpack: given string which signals how much data/size of data so 
#   it knows how to unpack it
#       => we pass the data: string


# print(data)







print("\n *** Program ran *** \n")