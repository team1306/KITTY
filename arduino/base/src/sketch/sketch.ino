bool onoff = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print("y");
  if(Serial.available() > 3) {
    int a = int(Serial.read());
    int b = int(Serial.read());
    int c = int(Serial.read());
    int d = int(Serial.read());
    if(a <= 127) {
      onoff = 0;
    }
    else {
      onoff = 1;
    }
  }
  if(onoff) {
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(13, LOW);
  }
}
