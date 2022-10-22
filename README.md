# Foot-Piano

## Introduction
This code was built for a foot piano, which we designed during Massachusetts Institute Of Technology's Edgerton Center Engineering Design Workshop 2022

<img src="https://content.instructables.com/ORIG/FH6/V3JW/L6F1TW04/FH6V3JWL6F1TW04.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=427ad86c71718e9b95ffd602d596b381">

Each button works with an ultrasonic sensor, which will send the distance between the top and bottom part of the button. If this data goes below a certain threshold, it will trigger a press by sending a 1.
After going through sensing all data from all ultrasonic sensors, the Arduino Code will send through serial the status of all sensors in a string containing all data divided by spaces.
## Usage & Features
This Code will convert binary data sent by an arduino through the serial port to sounds, which will vary depending on the button you step on.



# Installation
0. Check my [Instructables Explanation](https://www.instructables.com/Foot-Piano/) on how to design and build your own button and the wiring

1. Open the Arduino Files folder, open the sensor.ino file 

2. Inside the arduino file, specify how many sensors you're gonna use and add to the lists your pins.
```
#define NUM_SENS 1      Number of Ultrasonic Sensors

Pins in which you have plugged the trig pins
int trig_pins[NUM_SENS] = {Sensor_1_TrigPin, Sensor_2_TrigPin};

Pins in which you have plugged the echo pins  
int echo_pins[NUM_SENS] = {Sensor_1_EchoPin, Sensor_2_EchoPin};   

These last two lists must have the sensors in order, so if you have added the sensor's trig pin in the first position of the trig list, the first position of the echo list must be the echo pin of the same sensor.

int data[NUM_SENS] = {0, 0, ... As many times as the ammount of sensors};

float maxes[NUM_SENS] = {0, 0, ... As many times as the ammount of sensors};
```



3. Upload sensor.ino to the arduino board.

4. Open main.py and select the number of sensors and the COM port. The number of sensors represents how many buttons you have connected to the arduino and the COM port can be known from the arduino IDE (tools/board)

```
NUM_OF_SENSORS = 8 

COM = "COMX" in windows, "/dev/ttyACMX" in linux, X being a number
```

5. Each sound can be changed on the dictionary called "notes", where each number on the left represents the index of the button when receiving data 

```
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
```