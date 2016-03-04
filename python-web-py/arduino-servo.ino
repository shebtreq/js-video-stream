#include <Servo.h>

Servo myservo;

int pos = 0;
double incr = 36;

void setup() {
  myservo.attach(9);
  Serial.begin(9600);
  Serial.println("Power On");
}

void loop() {
  while(Serial.available() > 0) {
    char ch = Serial.read();
    double newPos = pos;
    if (ch == 'l') {
      newPos += incr;
      pos = newPos > 180 ? pos : newPos;
      Serial.println(pos);
      myservo.write(pos);
    }
    else if (ch == 'r') {
      newPos -= incr;
      pos = newPos < 0 ? pos : newPos;
      Serial.println(pos);
      myservo.write(pos);
    }
    delay(50);
  }  
}
