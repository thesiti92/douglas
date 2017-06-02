#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(3, 4);
volatile unsigned int revolutions;
unsigned int mph;
unsigned long lastmillis;

long oldPosition  = -999;
float old_speed = -999;
long newPosition = 0;
int sonar_pin = 0;
int stop_pin = 13;
int hall_pin = 0;

void setup() {
  Serial.begin(115200);
  attachInterrupt(hall_pin, update_rev, RISING); 
  revolutions = 0;
  mph = 0;
  lastmillis = 0;
  pinMode(stop_pin, OUTPUT);      // sets the digital pin as output

}
//analog scaling factor is .00500489=5 *(5.0 / 1023.0)--voltage conversion /(5/1024)--voltage scaling /1000--conversion to m from mm
void loop() {
  if(analogRead(sonar_pin)<599){ // 599 = .00500489/3 meters -- simplifying the inequality
    digitalWrite(stop_pin, HIGH);
  }
  else{
    digitalWrite(stop_pin, LOW);
  }
  newPosition = myEnc.read();
  // float current_speed=0; //mateen needs to get hall effect code for this to work, this should read in speed from hall sensor
  if (newPosition != oldPosition) {
    oldPosition = newPosition;
    Serial.println(String(newPosition*.0975) + " " + String(mph));
  }
  if (millis() - lastmillis>=1500){ //Uptade every one second, this will be equal to reading frecuency (Hz).
    detachInterrupt(0);//Disable interrupt when calculating
//    rpm = revolutions * 60; // Convert frecuency to RPM, note: this works for one interruption per full rotation.
    mph = revolutions*2.811; // revolutions * 60rpm * circumference in km * 60 to get kph * .6214 to get mph
    Serial.println(revolutions);
    Serial.println(String(newPosition*.0975) + " " + String(mph));
    revolutions = 0; // Restart the RPM counter
    lastmillis = millis(); // Uptade lasmillis
    attachInterrupt(0, update_rev, FALLING); //enable interrupt
  }
}
// I dont think we need this check after all if we have a 1 second latency
// if(abs(current_speed-old_speed)>1) {
//   Serial.println(String(newPosition*.0975) + " " + current_speed);
// }

 void update_rev()
 {
   revolutions++;

 }
