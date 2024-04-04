import librosa
import numpy as np

# Load the song
y, sr = librosa.load('Kalam_ink_isha3.0.wav')

# Separate the song into vocals and accompaniment
# This is a simple method that works well for some songs
vocals, accompaniment = librosa.decompose.nn_source_separation(y)

# Save the instrumental part of the song
librosa.output.write_wav('instrumental.wav', accompaniment, sr)