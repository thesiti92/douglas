#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(2, 3);

void setup() {
  Serial.begin(115200);
}

int mph = 50;

void loop() {
  Serial.println(String(myEnc.read()*.0975) + " " + mph);
}
