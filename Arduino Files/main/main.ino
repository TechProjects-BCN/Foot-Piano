
int trig_pins[] = {31};
int echo_pins[] = {30};
#define NUM_SENS 1
int data[] = {0};
int maxes[] = {0};
long t, hight;
float hight_0 = 3.2;

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
  Serial.begin(9600);
  for (int i = 0; i < NUM_SENS; i++) {
    pinMode(trig_pins[i], OUTPUT);
  }
  for (int i = 0; i < NUM_SENS; i++) {
    pinMode(echo_pins[i], INPUT);
  }
  for (int i = 0; i < NUM_SENS; i++) {
    maxes[i] = readData(trig_pins[i], echo_pins[i]);
  }
}

void loop() {
  String to_send = "";
  for (int i = 0; i < NUM_SENS; i++) {
    float distance = readData(trig_pins[i], echo_pins[i]);
    if (distance < maxes[i]-0.5) {
      data[i] = 1;
    } else {
      data[i] = 0;
    }
  }
  to_send = String(data[0]) + " "; //  + String(data[1]) + " " + String(data[2]) + " " + String(data[3]) + " " + String(data[4]);
  Serial.println(to_send);
  delay(300);
}
