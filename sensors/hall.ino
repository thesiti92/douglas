/*
Arduino Hall Effect Sensor Project
by Arvind Sanjeev
Please check out  http://diyhacking.com for the tutorial of this project.
DIY Hacking
*/


 volatile byte half_revolutions;
 unsigned int rpm;
 unsigned long timeold;
 float radius = 20.0
 float circ_cm = (2*math.pi)*radius  # calculate wheel circumference in CM


 void setup()
 {
   Serial.begin(115200);
   attachInterrupt(0, magnet_detect, RISING);//Initialize the intterrupt pin (Arduino digital pin 2)
   half_revolutions = 0;
   rpm = 0;
   timeold = 0;
 }
 void loop()//Measure RPM
 {
   if (half_revolutions >= 20) { 
     rpm = 30*1000/(millis() - timeold)*half_revolutions;
     timeold = millis();
     half_revolutions = 0;
     Serial.println(rpm,DEC);
     Serial.println(calculate_speed(rpm))
   }
 }
 void magnet_detect()//This function is called whenever a magnet/interrupt is detected by the arduino
 {
   half_revolutions++;
   Serial.println("detect");
 }

 float calculate_speed(rpm)
 {
    float dist_km = circ_cm/100000        # convert cm to km
    km_per_minute = dist_km * rpm      # calculate KM/sec
    km_per_hour = km_per_minute * 60      # calculate KM/h
    return km_per_hour 
 }