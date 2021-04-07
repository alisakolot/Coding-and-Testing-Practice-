import speech_recognition as s_r 
print(s_r.__version__)

# r = s_r.Recognizer()

# find mix devices attached to comp 
print(s_r.Microphone(list_microphone_names()))
# recognizer class
my_mic = s_r.Microphone(device_index = 1)
# stream = r.open(format=FORMAT, channels=1, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK_SIZE)

with my_mic as source:
    print("Say now!")
    audio = r.listen(source)


r.recognize_google(audio)
print(r.recognize_google(audio))









# https://www.codespeedy.com/get-voice-input-with-microphone-in-python-using-pyaudio-and-speechrecognition/