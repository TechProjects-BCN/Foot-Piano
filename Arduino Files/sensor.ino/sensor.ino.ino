
int trig_pins[] = {32, 34, 40, 44, 46, 48, 50, 52};
int echo_pins[] = {33, 35, 41, 45, 47, 49, 51, 53};
#define NUM_SENS 8
int data[] = {0, 0, 0, 0, 0, 0, 0, 0};
float maxes[] = {0, 0, 0, 0, 0, 0, 0, 0};
long t, hight;
float hight_0 = 1;

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
    delay(100);
    //Serial.print(maxes[i]);
    //Serial.println(" ");
  }
}

void loop() {
  String to_send = "";
  for (int i = 0; i < NUM_SENS; i++) {
    float distance = readData(trig_pins[i], echo_pins[i]);
    if (distance < maxes[i]-0.6) {
      data[i] = 1;
      //data[i] = distance + 10;
    } else {
      data[i] = 0;
      //data[i] = distance;
    }
  }
  to_send = String(data[0]) + " "  + String(data[1]) + " " + String(data[2]) + " " + String(data[3]) + " " + String(data[4]) + " " + String(data[5]) + " " + String(data[6])+ " " + String(data[7]);
  Serial.println(to_send);
  delay(100);
}
