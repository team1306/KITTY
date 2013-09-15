#include <Servo.h>

Servo s;
int pos = 20;

void setup() {
  Serial.begin(9600);
  delay(500);
  Serial.println("yodel");
  pinMode(13, OUTPUT);
}

void loop() {
  if(Serial.available() > 3) {
    int a = int(Serial.read());
    int b = int(Serial.read());
    int c = int(Serial.read());
    int d = int(Serial.read());
    pos = a;
    Serial.println("yodel");
  }
  if(pos > 127) {
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(13, LOW);
  }
}
