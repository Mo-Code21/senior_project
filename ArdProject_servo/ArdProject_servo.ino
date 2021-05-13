#include <Servo.h>
Servo myservo;
// 5-3-21
// Mohammed
// Motor with pressure sensor

// Including libraries:
#include "HX711.h"

// Sensor 
#define dataPin 2
#define sckPin 3

HX711 sensor;

// Motor 
// Define number of steps per revolution:
int pos = 0;

// Give the motor control pins names:
// motor 1
#define sPin 8


char uinput=0;


// Setup //////////////////////
void setup() {
  
  // Pressure sensor setup
  Serial.begin(57600);
  sensor.begin(dataPin, sckPin);
  
  // Motor Setup
  myservo.attach(8);
  
}


// Loop //////////////////////
void loop() {
  pressure();
  
  if (Serial.available() > 0) {
    
      uinput = Serial.read();
      
      if (uinput == 'r') {
          // Step one revolution in one direction:
          motor();
          Serial.println("motor moved");
          pressure();
          delay(500);
      }

      else {
          // Step one revolution in one direction:
          Serial.println("motor stoped?");
          pressure();
          delay(500);
    }
    uinput = '0';
    
    
    }
  
}
