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
    format = FORMAT, 
    channels = CHANNELS,
    rate = RATE, 
    input = True, 
    output = True,
    frames_per_buffer = CHUNK 
)
# stream object

'''GETTING BITS'''
data = stream.read(CHUNK)
# data object, when 'data' is run, you will get a bunch of bytes, but not integers  
    # can't plot in matplotlib, so you need to convert it 
    # [conversion using struct below]

'''BITS TO INT'''
# data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B',  data), dtype = 'b')[::2] + 127
# 'B': integer from 0 - 255
# adding 127/half the range values that are greater than 255 will wrap back around 
# [::2] : take every other point in array

# print(len(data)) # length of data is double what our chunk is
# print(data_int)# a tuple, int vals 0=255

# data_int obj will give us integer data instead of byte data
# unpack: given string which signals how much data/size of data so 
#   it knows how to unpack it
#       => we pass the data: string
fig, ax = plt.subplots ()

x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))
ax.set_ylim(0, 255) 
ax.set_xlim(0, CHUNK)


while True: 

    data = stream.read(CHUNK)
    data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B',  data), dtype = 'b')[::2] + 127

    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()


# ax.plot(data_int, '-')
# plt.show()

# print(data)







print("\n *** Program ran *** \n")