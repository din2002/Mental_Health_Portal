
from pyAudioAnalysis import audioSegmentation as aS
import os
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
dia={}

dia[301]=aS.speaker_diarization('data/processed/P302/P302_no_silence.wav',2)
print(dia)

#   c=0
#   dic={}
#   for j in dia[i[:3]]:
#     dic[c]=j
#     c+=1
#   del(dia[i[:3]])
#   dia[i[:3]]=dic 