

void motor() {
  // Activate motors
  // motor 1
  //digitalWrite(slp1Pin, HIGH);
  //digitalWrite(rst1Pin, HIGH);
  // motor 2
  //digitalWrite(slp2Pin, HIGH);
  //digitalWrite(rst2Pin, HIGH);
    
  // Set the spinning direction clockwise:
  // motor 1
  digitalWrite(dir1Pin, HIGH);
  // motor 2
  digitalWrite(dir2Pin, HIGH);

  // Spin the stepper motor 10 BOA steps
  for (int i = 0; i < 57; i++) {
    digitalWrite(step1Pin, HIGH);
    digitalWrite(step2Pin, HIGH);
    delayMicroseconds(500);
    digitalWrite(step1Pin, LOW);
    digitalWrite(step2Pin, LOW);
    delayMicroseconds(500);
  }
}
