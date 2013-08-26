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
    if(a >= 127) {
      onoff = 0;
    }
    else {
      onoff = 1;
    }
    Serial.println("yodel");
  }
  digitalWrite(11, onoff);
}
