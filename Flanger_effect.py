# play_vibrato_ver2.py
# Reads a specified wave file (mono) and plays it with a vibrato effect.
# (Sinusoidal time-varying delay)
# This implementation uses a circular buffer with two buffer indices.
# Uses linear interpolation

import pyaudio
import wave
import struct
import math
from myfunctions import clip16

# TRY BOTH WAVE FILES
WIDTH = 2           # bytes per sample
CHANNELS = 1        # mono
RATE = 8000
BLOCKLEN = 1024
DURATION = 10        # Duration in seconds

K = int( DURATION * RATE / BLOCKLEN )   # Number of blocks

print('Block length: ', BLOCKLEN)
print('Number of blocks to read: ', K)

# Vibrato parameters
f0 = 2
W = 0.2
gdepth = 0.2
# W = 0 # for no effct

# f0 = 10
# W = 0.2

# OR
# f0 = 20
# ratio = 1.06
# W = (ratio - 1.0) / (2 * math.pi * f0 )
# print W

# Create a buffer (delay line) for past values
buffer_MAX =  1024                          # Buffer length
buffer = [0.0 for i in range(buffer_MAX)]   # Initialize to zero

# Buffer (delay line) indices
kr = 0  # read index
kw = int(0.5 * buffer_MAX)  # write index (initialize to middle of buffer)
kw = buffer_MAX/2

# print('The delay of {0:.3f} seconds is {1:d} samples.'.format(delay_sec, delay_samples))
print('The buffer is {0:d} samples long.'.format(buffer_MAX))

# Open an output audio stream
p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)

stream = p.open(
    format = PA_FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = False)

# output_all = ''            # output signal in all (string)
output_all = bytes([])            # output signal in all (string)

print ('* Playing...')

# Loop through wave file 
for n in range(0, LEN):

    # Get sample from microphone input
    input_string = stream.read(BLOCKSIZE, exception_on_overflow=False)

    # Convert string to number
    input_value = struct.unpack('h' * BLOCKSIZE, input_string)

    # Get previous and next buffer values (since kr is fractional)
    kr_prev = int(math.floor(kr))               
    kr_next = kr_prev + 1
    frac = kr - kr_prev    # 0 <= frac < 1
    if kr_next >= buffer_MAX:
        kr_next = kr_next - buffer_MAX

    # Compute output value using interpolation
    output_value = (1-frac) * buffer[kr_prev] + frac * buffer[kr_next]

    # Update buffer (pure delay)
    buffer[int(kw)] = input_value

    # Increment read index
    kr = kr + 1 + W * math.sin( 2 * math.pi * f0 * n / RATE )
        # Note: kr is fractional (not integer!)

    # Ensure that 0 <= kr < buffer_MAX
    if kr >= buffer_MAX:
        # End of buffer. Circle back to front.
        kr = 0

    # Increment write index    
    kw = kw + 1
    if kw == buffer_MAX:
        # End of buffer. Circle back to front.
        kw = 0

    output_value += (input_value*gdepth)    

    # Clip and convert output value to binary string
    output_string = struct.pack('h', int(clip16(output_value)))

    # Write output to audio stream
    stream.write(output_string)

    output_all = output_all + output_string     # append new to total

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
wf.close()
