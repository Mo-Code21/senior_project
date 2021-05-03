// 2-23-21
// Edition 1.0
// motor control using IR remote

// Include the Stepper library:
#include <Stepper.h>


// Define number of steps per revolution:
const int stepsPerRevolution = 200;

// Give the motor control pins names:
#define pwmA 3
#define pwmB 11
#define brakeA 9
#define brakeB 8
#define dirA 12
#define dirB 13

char uinput=0;

// Initialize the stepper lib on the motor shield:
Stepper myStepper = Stepper(stepsPerRevolution, dirA, dirB);

void setup() 
{
  // Set the PWM and brake pins so that the direction pins can be used to control the motor:
  pinMode(pwmA, OUTPUT);
  pinMode(pwmB, OUTPUT);
  pinMode(brakeA, OUTPUT);
  pinMode(brakeB, OUTPUT);
  
  digitalWrite(pwmA, HIGH);
  digitalWrite(pwmB, HIGH);
  digitalWrite(brakeA, LOW);
  digitalWrite(brakeB, LOW);
  
  
  // Set the motor speed (RPMs):
  myStepper.setSpeed(60);

  Serial.begin(9600);
}


void loop() 
{
    if (Serial.available() > 0) {
      uinput = Serial.read();
      
      if (uinput == 'r') {
          // Step one revolution in one direction:
          myStepper.step(57);
          Serial.println("motor moved?");
          delay(1000);
      }

      else {
          // Step one revolution in one direction:
          myStepper.step(0);
          Serial.println("motor stoped?");
          delay(1000);
    }
    uinput = '0';
    
    }
}
