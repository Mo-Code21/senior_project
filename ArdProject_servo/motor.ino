

void motor() {
  // Activate motors
  // motor 1
  //digitalWrite(slp1Pin, HIGH);
  //digitalWrite(rst1Pin, HIGH);
  // motor 2
  //digitalWrite(slp2Pin, HIGH);
  //digitalWrite(rst2Pin, HIGH);
    
  // Set the spinning direction clockwise:
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);              
      delay(15);                       // waits 15ms for the servo to reach the position
    }
}
