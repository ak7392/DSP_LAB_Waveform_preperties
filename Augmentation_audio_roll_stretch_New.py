import librosa
import numpy as np
import glob
import os

WIDTH = 2       # Number of bytes per sample
CHANNELS = 1    # mono
RATE = 8000 


file_ext="*.wav"
sub_dirs = ["data_roll"]
sub_dirs2 = ["data_stretch"]
parent_dir = "output"


for label, sub_dir in enumerate(sub_dirs):
    for fn in glob.glob(os.path.join(parent_dir, sub_dir, file_ext)):
        labels   = (fn.split('\\')[2].split('_')[0])
        labels1 = (fn.split('\\')[2].split('_')[1])
        labels2 = (fn.split('\\')[2].split('_')[2])
        labels3 = (fn.split('\\')[2].split('_')[3])
        labels4 = (fn.split('\\')[2].split('_')[4].split('.')[0])
        name1 = ('output2/' + labels + '_' + labels1 + '_' + labels2 + '_' + labels3 + '_' + labels4  + '.wav')

        wf1 = wave.open(name1, 'wb')
        wf1.setnchannels(CHANNELS)
        wf1.setsampwidth(WIDTH)
        wf1.setframerate(RATE)
        p = pyaudio.PyAudio()

        wf = wave.open(fn, 'rb')
        input_string = wf.readframes(1)

        print("start")


        while(len(input_string)) > 0:

              
            input_tuple = struct.unpack('h', input_string)[0]

            output_string = struct.pack('h', input_tuple)
            wf1.writeframes(output_string)

            input_string = wf.readframes(1)


for label, sub_dir in enumerate(sub_dirs2):
    for fn in glob.glob(os.path.join(parent_dir, sub_dir, file_ext)):
        labels   = (fn.split('\\')[2].split('_')[0])
        labels1 = (fn.split('\\')[2].split('_')[1])
        labels2 = (fn.split('\\')[2].split('_')[2])
        labels3 = (fn.split('\\')[2].split('_')[3])
        labels4 = (fn.split('\\')[2].split('_')[4].split('.')[0])
        name1 = ('output2/' + labels + '_' + labels1 + '_' + labels2 + '_' + labels3 + '_' + labels4  + '.wav')

        wf1 = wave.open(name1, 'wb')
        wf1.setnchannels(CHANNELS)
        wf1.setsampwidth(WIDTH)
        wf1.setframerate(RATE)
        p = pyaudio.PyAudio()

        wf = wave.open(fn, 'rb')
        input_string = wf.readframes(1)

        print("start")


        while(len(input_string)) > 0:

              
            input_tuple = struct.unpack('h', input_string)[0]

            output_string = struct.pack('h', input_tuple)
            wf1.writeframes(output_string)

            input_string = wf.readframes(1)

