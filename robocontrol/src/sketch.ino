#include <Servo.h>

int s = 0;
unsigned long t = 0;

Servo j;

void setup() {
  j.attach(9);
  Serial.begin(115200);
  Serial.print("yodel");
  t = millis();
}

void loop() {
  if(Serial.available() > 0) {
    s = int(Serial.read());
    t = millis();
  }
  if(millis() - t < 500) {
    j.writeMicroseconds(83*s/10 + 670);
  }
  else {
    digitalWrite(9, LOW);
  }
}