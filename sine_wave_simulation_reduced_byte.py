from struct import pack
from math import sin, pi
import wave

Fs = 8000        

sine_wave = wave.open('sine_wave_simulation_reduced_byte.wav', 'w')		# appending data on sine wave file

sine_wave.setnchannels(1)         # one channel (mono)

sine_wave.setframerate(Fs)        # samples per second for the sine wave

sine_wave.setsampwidth(1)		 #  sample width is 1 byte (8 bits) per sample for this wave


N = int(0.5*Fs)						
			
A = 2**7 - 1.0 			# Amplitue of the wave 

f = 260.1					# frequency of the wave in hertz

for n in range(0, N):	    
	x = A * (sin(2*pi*f/Fs*n)+ 1)       	# equation for the wave function
	byte_string = pack('B', int(x))   
	sine_wave.writeframes(byte_string)
sine_wave.close()