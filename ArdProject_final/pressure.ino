
void pressure() {
  
  if (sensor.is_ready()) {
    long reading = sensor.read();
    Serial.println(reading);   // printing raw data
    }
  
    else{
      Serial.println(0);
    }

 // sensor.power_down
}
