// DEPRECATED - ended up replacing Arduino with Photon



// Author: Jeremy Phillips
// License: GPL
// Version 2016.10.19.1
// Email: code@cloudcrier.com

// Description: Monitor an input for state change, counting the number of state changes.  
// Purpose:  In this scenario, the sketch is used with a hall effect sensor (magnetic field sensor) to detect when a magnet attached to a flywheel passes by.  By counting the state changes per minute of the input (rpm of flywheel), by extension can calculate the mph of flywheel. 

// reference - http://www.microsmart.co.za/technical/2014/03/01/advanced-arduino-adc/


// Libraries
//#include <Wire.h>

// Variables
unsigned long startTime;
unsigned long stopTime;
unsigned int stateCount; // count of state changes
unsigned int prevStateCount; // Previous count of state changes before resetting to 0;

// Constants
byte sensorInput = 2; // The input that has a sensor to detect event; note:  for UNO, must be pin 2 or 3
bool enableDebug = true; // If printing debug info to serial
byte busAddress = 2; // Define i2v bus address

void setup() {
  // If debug mode enable, setup serial
  if(enableDebug) {
    Serial.begin(9600);
  }

  // Setup i2c protocol
  Wire.begin(busAddress);
  Wire.onRequest(sendState);
  
  // Setup input mode for pullup of hall sensor
  pinMode(sensorInput, INPUT_PULLUP);
  
  // Setup interrupt to sensor pin when event is finishing (has dropped ping low, then rising back)
  attachInterrupt(digitalPinToInterrupt(sensorInput), sensorStateChange, RISING); 

  // initialize variables
  stateCount = 0;
  startTime = micros();
  stopTime = micros();
}

void loop() {
//  for (int i=9; i > 0; i--) {
//    runningStateCount[i]=runningStateCount[i-1];
//  }

  if(enableDebug) {
    printDebug();
  }
  delay(10000);
}

void sensorStateChange () {
  stateCount += 1;  
  if(enableDebug) {
    Serial.println("Interrupted!");
    //printDebug();
  }
}

void printDebug () {
  stopTime = micros();
  Serial.print("Time: ");
  Serial.print(stopTime - startTime);
  Serial.print("μs  Count: ");
  Serial.print(stateCount);
  //Serial.print("  State: ");
  //Serial.print(digitalRead(sensorInput));
  Serial.print("\n");
  startTime = micros();
}

void sendState() {
  prevStateCount = stateCount;
  stateCount = 0;
  Wire.write(prevStateCount);
}

