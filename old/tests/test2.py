import serial

ard = serial.Serial('COM6')
while True:
    _received = ard.readline()
    data = _received.split()
    print(data)