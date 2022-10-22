
#define NUM_SENS 1
// The length of all these lists must be the same as NUM_SENS
int trig_pins[NUM_SENS] = {10};
int echo_pins[NUM_SENS] = {9};
int data[NUM_SENS] = {0};
float maxes[NUM_SENS] = {0};

// Variables for calculating the distance
// measured by the ultrasonic sensors
long t, hight;
float hight_0 = 1;

// This function will calculate the distance
// from the data received by the ultrasonic
// sensor and return it
float readData(int TRIG_PIN, int ECHO_PIN){
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  float duration= pulseIn(ECHO_PIN, HIGH);
  return duration * 0.034 / 2;
  }

void setup() {
  // Definitions of Pins on the arduino
  Serial.begin(9600);
  for (int i = 0; i < NUM_SENS; i++) {
    pinMode(trig_pins[i], OUTPUT);
  }
  for (int i = 0; i < NUM_SENS; i++) {
    pinMode(echo_pins[i], INPUT);
  }
  // Autocalibration (Setting up the 0)
  for (int i = 0; i < NUM_SENS; i++) {
    maxes[i] = readData(trig_pins[i], echo_pins[i]);
    delay(100);
    //Serial.print(maxes[i]);
    //Serial.println(" ");
  }
}

void loop() {
  // string to send to our computer
  String to_send = "";
  // Reading all distances and if they are within
  // a threshold, sending a one to our computer
  for (int i = 0; i < NUM_SENS; i++) {
    float distance = readData(trig_pins[i], echo_pins[i]);
    if (distance < maxes[i]-0.6) {
      data[i] = 1;
    } else {
      data[i] = 0;
    }
  }
  // Sending the data to our arduino
  to_send = String(data[0]) + " "; // + String(data[1]) + " " + String(data[2]) + " " + String(data[3]) + " " + String(data[4]) + " " + String(data[5]) + " " + String(data[6])+ " " + String(data[7]);
  Serial.println(to_send);
  delay(100);
}
