//Polls all sensor data from the kart and pushes it to the Pi through a serial connection
//Sensors include: Hall effect for speed, encoder for steering motor position (using a handy encoder library),
//and a sonar sensor for auto-breaking

#include <Encoder.h>

Encoder myEnc(3, 4);
volatile unsigned int revolutions;
unsigned long lastmillis;
float last = 0;
float timeElapsed = 0;
float circ = .6723;
float mph;
float last_mph;
float mph_conversion = circ * 2.23694*1000;

long oldPosition  = -999;
float old_speed = -999;
long newPosition = 0;
int sonar_pin = 0;
int stop_pin = 13;
int hall_pin = 0;

void setup() {
  Serial.begin(115200);
//  attachInterrupt(hall_pin, update_mph, RISING); 
  revolutions = 0;
  mph = 0;
  lastmillis = 0;
  pinMode(stop_pin, OUTPUT);      // sets the digital pin as output
  last = millis();


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
}
// I dont think we need this check after all if we have a 1 second latency
// if(abs(current_speed-old_speed)>1) {
//   Serial.println(String(newPosition*.0975) + " " + current_speed);
// }

 void update_mph()
 {
   timeElapsed = millis() - last;
   mph = mph_conversion/timeElapsed;
   if(mph!=last_mph){
       Serial.println(String(newPosition*.0975) + " " + String(mph));
       last_mph = mph;
   }
   last = millis();
 }
