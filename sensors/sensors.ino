#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(2, 3);

void setup() {
  Serial.begin(115200);
}

long oldPosition  = -999;
int mph = 0;

void loop() {
  long newPosition = myEnc.read();
  if (newPosition != oldPosition) {
      oldPosition = newPosition;
      Serial.println(String(newPosition*.0975) + " " + mph);

  }
}
