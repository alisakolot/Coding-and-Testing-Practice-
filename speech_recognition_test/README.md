TROUBLESHOOTING: 

1.  'OSError: [Errno -9998] Invalid number of channels'

stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK_SIZE)
    - doesn't recognize p
    - when switched p to r, Recognizer does not have attribute open 
    