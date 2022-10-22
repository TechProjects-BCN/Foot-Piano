int Buttons[] = {2, 3};
int data[]= {0, 0};

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < 2; i++){
    pinMode(Buttons[i], INPUT);
    }
  Serial.begin(9600);
}

void loop() {
  for(int i = 0; i < 2; i++){
    if (digitalRead(Buttons[i]){
      data[i] = 1;
      }else{
      data[i] = 0;
        }
    }
    String to_send = data[0] + " " + data[1];
   Serial.println(to_send)
}
