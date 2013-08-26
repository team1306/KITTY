#include <Servo.h>

Servo s;
int pos = 0;

void setup() {
  Serial.begin(9600);
  delay(500);
  Serial.println("yodel");
  pinMode(11, OUTPUT);
  s.attach(9);
}

void loop() {
  if(Serial.available() > 3) {
    int a = int(Serial.read());
    int b = int(Serial.read());
    int c = int(Serial.read());
    int d = int(Serial.read());
    pos = int(180*a/255);
    Serial.println("yodel");
  }
  s.write(pos);
}
