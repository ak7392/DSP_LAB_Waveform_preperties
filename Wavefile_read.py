
import wave

audio = wave.open('abhi.wav')

print(audio.getnchannels()) 
# number of channels

print(audio.getframerate()) 
# frame rate (number of frames per second)

print(audio.getnframes()) 
# total number of frames (length of signal)

print(audio.getsampwidth()) 
# number of bytes per frame

audio.close()
