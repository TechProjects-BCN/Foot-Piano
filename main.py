import time
import threading
import serial
import numpy as np
import sounddevice as sd
import time
import pygame

pygame.init()
clock = pygame.time.Clock()
status = [0, 0, 0, 0, 0, 0, 0]
# Sounds

notes= {
    6:pygame.mixer.Sound("A.wav"),
    1:pygame.mixer.Sound("B.wav"),
    5:pygame.mixer.Sound("C.wav"),
    0:pygame.mixer.Sound("D.wav"),
    7:pygame.mixer.Sound("E.wav"),
    4:pygame.mixer.Sound("F.wav"),
    2:pygame.mixer.Sound("G.wav"),
    3:pygame.mixer.Sound("F#.wav")
} 

data = []

ard = serial.Serial('/dev/ttyACM0')

class Main:
    def __init__(self):
        self.to_play = []
    def server_arduino(self):
        while True:
            _received = ard.readline()
            data = _received.split()
            print(data)
            for index, sensor in enumerate(data):
                    if int(sensor) == 1 and status[index] != 1:
                        status[index] = 1
                        self.to_play.append(notes[index])
                    elif int(sensor) == 0:
                        status[index] = 0
            time.sleep(0.05)

    def server_tone(self):
        while True:    
            #print(self.to_play)
            for index, note in enumerate(self.to_play):
                pygame.mixer.Channel(index).play(note)
            self.to_play = []
            time.sleep(0.05)
                

_main = Main()
threading.Thread(target=_main.server_arduino, args=()).start()
threading.Thread(target=_main.server_tone, args=()).start()