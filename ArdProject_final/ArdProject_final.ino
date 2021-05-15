// 5-14-21
// Mohammed
// Motor with pressure sensor for final product

// Including libraries:
#include "HX711.h"

// Sensor 
#define dataPin 2
#define sckPin 3

HX711 sensor;

// Motor 
// Define number of steps per revolution:
const int stepsPerRevolution = 200;

// Give the motor control pins names:
// motor 1
#define step1Pin 11
#define dir1Pin 12
// #define slp1Pin 10
// #define rst1Pin 10
// motor 2
#define step2Pin 8
#define dir2Pin 9
// #define slp2Pin 7
// #define rst2Pin 7

char uinput=0;


// Setup //////////////////////
void setup() {
  
  // Pressure sensor setup
  Serial.begin(57600);
  sensor.begin(dataPin, sckPin);

  // Motor Setup
  // Set the PWM and brake pins so that the direction pins can be used to control the motor:
  // motor 1
  pinMode(step1Pin, OUTPUT);
  pinMode(dir1Pin, OUTPUT);
  // motor 2
  pinMode(step2Pin, OUTPUT);
  pinMode(dir2Pin, OUTPUT);
  
}
///////////////////////
// I need to fix the pressure function to convert bytes to pressure values using calibrated equation
// carry the pressure values to the main script and add it to the if statements

// Loop //////////////////////
void loop() {

   // Running the pressure function
  pressure();

  // controlling the motor
  if (Serial.available() > 0) {
      uinput = Serial.read();
      
      if (uinput == 'r' && ) {
          // Step one revolution in one direction:
          motor();

          delay(500);
      }

            if (uinput == 'o' && ) {
          // Step one revolution in one direction:
          motor();

          delay(500);
      }

            if (uinput == 't' && ) {
          // Step one revolution in one direction:
          motor();

          delay(500);
      }

            if (uinput == 'h' && ) {
          // Step one revolution in one direction:
          motor();

          delay(500);
      }

            if (uinput == 'f' && ) {
          // Step one revolution in one direction:
          motor();

          delay(500);
      }

      else {
          // Rest for some time
          delay(500);
    }
    uinput = '0';
    
    }
  
}
