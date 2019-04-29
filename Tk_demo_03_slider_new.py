# Tk_demo_03_slider.py
# TKinter demo
# Play a sinusoid using Pyaudio. Use two sliders to adjust the frequency and gain.

from math import cos, pi 
import pyaudio
import struct
import sys
import numpy as np

if sys.version_info[0] < 3:
	# for Python 2
	import Tkinter as Tk
else:
	# for Python 3
	import tkinter as Tk   	

def fun_quit():
  global PLAY
  print('I quit')
  PLAY = False

Fs = 8000     # rate (samples/second)
gain = 0.2 * 2**15

# Define Tkinter root
top = Tk.Tk()

# Define Tk variables
f1 = Tk.DoubleVar()
gain = Tk.DoubleVar()

# Initialize Tk variables
f1.set(200)   # f1 : frequency of sinusoid (Hz)
gain.set(0.2 * 2**15)

# Define buttons
S_freq = Tk.Scale(top, label = 'Frequency', variable = f1, from_ = 100, to = 400, tickinterval = 100)
S_gain = Tk.Scale(top, label = 'Gain', variable = gain, from_ = 0, to = 2**15-1)
Bquit = Tk.Button(top, text = 'Quit', command = fun_quit)
MAXVALUE = 2**15-1

# Place buttons
Bquit.pack(side = Tk.BOTTOM, fill = Tk.X)
S_freq.pack(side = Tk.LEFT)
S_gain.pack(side = Tk.LEFT)

# Create Pyaudio object
p = pyaudio.PyAudio()
stream = p.open(
  format = pyaudio.paInt16,  
  channels = 1, 
  rate = Fs,
  input = False, 
  output = True,
  frames_per_buffer = 128)            
  # specify low frames_per_buffer to reduce latency

theta = 0
PLAY = True

BLOCKLEN = 256
output_block = [0 for n in range(0, BLOCKLEN)]
new_output_block = [0 for n in range(0, BLOCKLEN)]
Final_output = [0 for n in range(0, BLOCKLEN)]
  

print('* Start')
while PLAY: 
  o_gain = gain.get()
  top.update()

  n_gain = gain.get() 

  om1 = 2.0 * pi * f1.get() / Fs
  if (n_gain != o_gain):
    diff = n_gain - o_gain
    for i in range(0, BLOCKLEN):
      theta = theta + om1
      
      o_gain = o_gain + (diff / BLOCKLEN)
      output_block[i] = int(o_gain * cos(theta))  
      output_block[i] = np.clip(output_block[i], -MAXVALUE, +MAXVALUE)
      output_block[i] = output_block[i].astype(int)

  else: 
    for i in range(0, BLOCKLEN):
      theta = theta + om1
      
      output_block[i] = int(n_gain * cos(theta))      
      output_block[i] = np.clip(output_block[i], -MAXVALUE, +MAXVALUE)
      output_block[i] = output_block[i].astype(int)

  if theta > pi:
    theta = theta - 2.0 * pi
  binary_data = struct.pack('h' * BLOCKLEN, *output_block)   # 'h' for 16 bits
  stream.write(binary_data)
print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
