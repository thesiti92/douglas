#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(2, 3);
volatile byte revolutions;
unsigned int mph;
unsigned long lastmillis;

long oldPosition  = -999;
float old_speed = -999;
long newPosition = 0;

void setup() {
  Serial.begin(115200);
  attachInterrupt(0, update_rev, RISING);
  revolutions = 0;
  mph = 0;
  lastmillis = 0;
}

void loop() {
  newPosition = myEnc.read();
  // float current_speed=0; //mateen needs to get hall effect code for this to work, this should read in speed from hall sensor

  if (newPosition != oldPosition) {
    oldPosition = newPosition;
    Serial.println(String(newPosition*.0975) + " " + mph);
  }
  if (millis() - lastmillis == 1000){ //Uptade every one second, this will be equal to reading frecuency (Hz).
    get_mph();
  }
}
// I dont think we need this check after all if we have a 1 second latency
// if(abs(current_speed-old_speed)>1) {
//   Serial.println(String(newPosition*.0975) + " " + current_speed);
// }

 void update_rev()
 {
   revolutions++;
   //Each rotation, this interrupt function is run twice
 }
 void get_mph(){
   detachInterrupt(0);//Disable interrupt when calculating
   // rpm = revolutions * 60; // Convert frecuency to RPM, note: this works for one interruption per full rotation.
   mph = revolutions*2.811; // revolutions * 60rpm * circumference in km * 60 to get kph * .6214 to get mph
   Serial.println(String(newPosition*.0975) + " " + mph);
   revolutions = 0; // Restart the RPM counter
   lastmillis = millis(); // Uptade lasmillis
   attachInterrupt(0, update_rev, FALLING); //enable interrupt
 }
