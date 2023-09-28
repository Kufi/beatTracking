import essentia
import numpy
from essentia.standard import *
 
audiobeat = MonoLoader(filename='./music.mp3')

rhythm_extractor = RhythmExtractor2013(method="multifeature")
bpm, beats, b_conf, _, _ = rhythm_extractor(audiobeat)
print("BPM:", bpm)
print("Beat positions (sec.):", beats) # Beat positions in seconds
print("Beat estimation confidence:", b_conf)

# extractor = essentia.standard.RhythmExtractor2013(method="multifeature")
# bpm = extractor(audiobeat)

# print(bpm)