from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
import os


# dir_name = r'C:/Dinesh/SEM-VI/RBL/Mental_Health_Portal/data/processed/P301'
# for file in os.listdir(dir_name):
#     file=os.path.join(dir_name,file)
samplerate, data = read('data/raw/audio/301_AUDIO.wav')
duration = len(data)/samplerate
time = np.arange(0,duration,1/samplerate)
plt.plot(time,data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()