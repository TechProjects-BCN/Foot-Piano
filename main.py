#!/usr/bin/env/ python3
# -*- coding: UTF-8 -*-
###########################
###
### 					   Foot-Piano's Driver
### 
###                           July 29th, 2022
###
### Purpose: We created this code to play a foot piano we designed
###          during the EDW 2022. This code converts the binary data
###          sent by the arduino into sounds using pygame's sound
###          library
###
### NOTES: I used python 3.9.7 to code this. It has been tested on python 3.9.13, but not 3.10
###
### Author:   Joel Garcia (@Newtoniano20 / Newtoniano#1173 on discord)
###           Webpage: https://newtoniano20.github.io/
### 
### GitHub:  https://github.com/Newtoniano20/Foot-Piano
###
### License:  MIT
### 
###########################

import threading
import serial
import time
import pygame


# Global Variables

# Number of sensors / buttons used
NUM_OF_SENSORS = 1

# Port used for the connection wth the arduino
# you can check which one the arduino is using in
# the arduino IDE tools/board
COM = "COM3"

# We initialize pygame, which we'll use to play sounds using
# It's sound library
pygame.init()
clock = pygame.time.Clock()

# We initialize a list where we'll store the data sent by the 
# arduino
# This list will be used to avoid playing a sound multiple times,
# so we'll store the last known value and compare it to the new one
status = [0 for x in range(NUM_OF_SENSORS)]

# This dictionary contains the data for each sound
notes = {
    0: pygame.mixer.Sound("audio_files/A.wav"),
    1: pygame.mixer.Sound("audio_files/B.wav"),
    2: pygame.mixer.Sound("audio_files/C.wav"),
    3: pygame.mixer.Sound("audio_files/D.wav"),
    4: pygame.mixer.Sound("audio_files/E.wav"),
    5: pygame.mixer.Sound("audio_files/F.wav"),
    6: pygame.mixer.Sound("audio_files/G.wav"),
    7: pygame.mixer.Sound("audio_files/F#.wav")
} 

# As we are going to use Threading and we need to share variables 
# between these threads, we'll create a class where we'll store 
# all variables and functions inside
class Main:
    # This is the data buffer, where raw data from the arduino will be
    # stored. 
    data = []

    def __init__(self, com):
        # Here we will store what needs to be played.
        # Once played, that sound will be removed.
        # This data will be the only thing shared between the 
        # two threads
        self.to_play = []
        # We create the arduino object from the class & using the 
        # specified port
        self.ard = serial.Serial(com)

    def server_arduino(self):
        """
        This will be the thread reading the data incoming from the 
        arduino and storing it into the variable 'data'
        """
        while True:
            # we read data from the arduino
            data = self.ard.readline().split()
            print(data)
            # this for loop will compare the data between the new
            # and old. This is made because we only want to play a
            # sound once, so if we already played something the last
            # time, it will not be sent to the other thread.
            for index, sensor in enumerate(data):
                if int(sensor) == 1 and status[index] != 1:
                    status[index] = 1
                    # here we add to the shared function what we
                    # want to play
                    self.to_play.append(notes[index])
                elif int(sensor) == 0:
                    status[index] = 0
            time.sleep(0.05)

    def server_tone(self):
        """
        This will be the thread that will play all sounds
        that appear in the variable to_play, added by the 
        server_arduino function
        """
        while True:
            # we loop for every note and play the sound
            # we will use the index on the list as the 
            # channel number
            for index, note in enumerate(self.to_play):
                pygame.mixer.Channel(index).play(note)
            # we reset the list, as we've already played those notes
            self.to_play = []
            time.sleep(0.05)


if __name__ == '__main__':
    # we create the object _main from the class Main
    _main = Main(com=COM)
    # We start the threads
    threading.Thread(target=_main.server_arduino, args=()).start()
    threading.Thread(target=_main.server_tone, args=()).start()
