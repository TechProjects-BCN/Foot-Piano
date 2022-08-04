import numpy as np
import sounddevice as sd
import time

def play_note(freq_hz, duration_s):
    # Samples per second
    sps = 44100

    # Attenuation so the sound is reasonable
    atten = 0.5

    # NumpPy magic to calculate the waveform
    each_sample_number = np.arange(duration_s * sps)
    waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
    waveform_quiet = waveform * atten

    # Play the waveform out the speakers
    sd.play(waveform_quiet, sps)
    time.sleep(duration_s)

play_note(256, 1)
sd.stop()
