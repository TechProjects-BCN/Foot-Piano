import time
import threading
import serial
import numpy as np
import sounddevice as sd
import time

#         A3      B3       C4      D4      E4      F4    G4
notes = [456.82, 439.71, 431.87, 417.48, 404.66, 398.79, 388.01, 300]
atten = 0.5
sps = 44100


def new_sine_wave(freq_hz, duration_s):
    each_sample_number = np.arange(duration_s * sps)
    waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
    return waveform * atten

data = []

ard = serial.Serial('/dev/ttyACM0')

class Main:
    def __init__(self):
        self.to_play = []
    def server_arduino(self):
        while True:
            if self.to_play != []:
                self.to_play = []
            _received = ard.readline()
            data = _received.split()
            #print(data)
            for index, sensor in enumerate(data):
                try:
                    #print(f"Sensor {index} is {sensor}")
                    if int(sensor) == 1:
                        self.to_play.append(new_sine_wave(freq_hz=notes[index], duration_s=1))
                        print(f"Playing note with frequency {notes[index]} in index {index} ")
                except:
                    pass
            time.sleep(0.3)

    def server_tone(self): 
        _wave = np.sin(0)
        while True:    
            print(self.to_play)
            for wave in self.to_play:
                _wave = _wave + wave
            _wave = _wave / len(self.to_play)
            #print("Wave : ", _wave)
            sd.play(_wave, sps)
            time.sleep(0.3)
            _wave = np.sin(0)
                

_main = Main()
threading.Thread(target=_main.server_arduino, args=()).start()
threading.Thread(target=_main.server_tone, args=()).start()