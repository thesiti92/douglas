
int hallPin = 1
int radarPin = 2
float last = 0;
float timeElapsed = 0;
float radius = 14; //in centimeters
float circ = 2*3.14159265358979323846264338327950*radius;
float dist = 0;
float velocity = 0;
int pulses = 0;
const int anPin = 0; 
long anVolt, mm, inches; 


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  attachInterrupt(0, magnet_detect, RISING);//Initialize the intterrupt pin (Arduino digital pin 2)

  pinMode(1,INPUT);  
  
}

void loop() {

  read_sensor(); 
  print_range();
  //if hall sensor pin is high or low (which is which?) then call calculate speed
  attachInterrupt(digitalPinToInterrupt(3),magnet_detect(),RISING);
  delay(100); 

   /*
   * RADAR
   * get input voltage
   * multiply by 5 and divide by 0.004883 to get distance in mm (divide by 1000 to get meters)
   */
  //RADAR:
}

void read_sensor (){ 
  anVolt = analogRead(anPin); 
  mm = anVolt*(5/0.004883); //Takes bit count and converts it to mm 
  inches = mm/25.4; //Takes mm and converts it to inches 
}

void print_range (){ 
  Serial.print("S1"); 
  Serial.print("="); 
  Serial.print(mm); 
  Serial.print(" "); 
  Serial.println(inches); 
}

void magnet_detect()//This function is called whenever a magnet/interrupt is detected by the arduino
 {
   pulses++;
   timeElapsed = millis() - last;
   dist += circ;
   velocity = circ / (100*1000*timeElapsed); // *100 to go from cm to m, *1000 for millisecond to second
   last = millis();
   Serial.println("Speed: ", velocity, " meters/sec");
 }


