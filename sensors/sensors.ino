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
float old_speed = -999;


void loop() {
  long newPosition = myEnc.read();
  float current_speed=0; //mateen needs to get hall effect code for this to work, this should read in speed from hall sensor 

  if (newPosition != oldPosition) {
      oldPosition = newPosition;
      Serial.println(String(newPosition*.0975) + " " + mph);
  }
  if(current_speed-old_speed<-1) {
  Serial.println(String(newPosition*.0975) + " " + mph);
  }else {
  	if (current_speed-oldspeed>1){
  	Serial.println(String(newPosition*.0975) + " " + mph);
  	}

  }
  


}
