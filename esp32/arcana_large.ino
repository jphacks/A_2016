#include "HX711.h"

// HX711 circuit wiring


const int LOADCELL_DOUT_PIN = 32;
const int LOADCELL_SCK_PIN = 33;

HX711 scale;

void setup() {
  
  Serial.begin(57600);
  Serial.print("[initiated]");
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
}

void loop() {

  if (scale.is_ready()) {
    long reading = scale.read_average(10);
    Serial.print("HX711 reading: ");
    Serial.println(reading);
    Serial.print("Weight estimation: ");
    long A=411790.393;
    long B=108114.4105;
    Serial.print((float(reading)-float(B))/float(A));
    Serial.println("[kg]");
  } else {
    Serial.println("HX711 not found.");
  }

  delay(1000);
  
}
