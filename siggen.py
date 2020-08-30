import wave, struct
import numpy as np
from scipy import signal as sg

sampling_rate = 44100                    ## Sampling Rate
freq = 400                             ## Frequency (in Hz)
samples = 441000                          ## Number of samples 
outputfile=r"C:\Users\xxx\Desktop\sawtooth_wave_400Hz_duty.wav"
amplitude=10000


#______________________________________________________________________________
x=np.arange(samples)
####### sine wave ###########
#y = amplitude*np.sin(2 * np.pi * freq * x / sampling_rate)

####### square wave ##########
#y = amplitude* sg.square(2 *np.pi * freq *x / sampling_rate)

####### square wave with Duty Cycle ##########
#y = amplitude* sg.square(2 *np.pi * freq *x / sampling_rate , duty = 0.8)

####### Sawtooth wave ########
y = amplitude* sg.sawtooth(2 *np.pi * freq *x / sampling_rate )

#______________________________________________________________________________
# Save to wave file, readable by any player
obj = wave.open(outputfile,'w')
obj.setnchannels(1) #Set the number of channels. 1 for Mono 2 for stereo channels
obj.setsampwidth(2) #Set the sample width to n bytes.
obj.setframerate(sampling_rate)

for i in range(samples):
   value = y[i]
   data = struct.pack('<h', int(value))
   obj.writeframesraw( data )

obj.close()