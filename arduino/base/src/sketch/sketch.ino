bool onoff = 0;

void setup() {
  Serial.begin(9600);
  delay(500);
  Serial.println("yodel");
  pinMode(11, OUTPUT);
}

void loop() {
  if(Serial.available() > 3) {
    int a = int(Serial.read());
    int b = int(Serial.read());
    int c = int(Serial.read());
    int d = int(Serial.read());
    Serial.println(a);
    Serial.println(b);
    Serial.println(c);
    Serial.println(d);
    if(a >= 127) {
      onoff = 0;
    }
    else {
      onoff = 1;
    }
  }
  digitalWrite(11, onoff);
}
