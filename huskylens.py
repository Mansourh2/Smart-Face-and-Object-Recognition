#include "HUSKYLENS.h"
#include "SoftwareSerial.h"

HUSKYLENS huskylens;
SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  while (!huskylens.begin(mySerial)) {
    Serial.println(F("HuskyLens not connected!"));
    delay(1000);
  }

  huskylens.writeAlgorithm(ALGORITHM_FACE_RECOGNITION);
  Serial.println(F("Face Recognition Mode"));
}

void loop() {
  if (huskylens.request()) {
    if (huskylens.available()) {
      HUSKYLENSResult result = huskylens.read();
      Serial.print("Face ID: ");
      Serial.println(result.ID);
      Serial.print("X: "); Serial.print(result.xCenter);
      Serial.print(" Y: "); Serial.println(result.yCenter);
    }
  } else {
    Serial.println("Failed to read from HuskyLens");
  }

  delay(200);
}