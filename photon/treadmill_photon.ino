// Author: Jeremy Phillips
// License: GPL
// Version 2016.10.19.1
// Email: code@cloudcrier.com

// Description: Monitor an input for state change, counting the number of state changes.
// Purpose:  In this scenario, the sketch is used with a hall effect sensor (magnetic field sensor) to detect when a magnet attached to a flywheel passes by.  By counting the state changes per minute of the input (rpm of flywheel), by extension can calculate the mph of flywheel.

// reference - http://www.microsmart.co.za/technical/2014/03/01/advanced-arduino-adc/


// Libraries
//

// Variables
unsigned long startTime;
unsigned long stopTime;
unsigned int stateCount; // count of state changes
unsigned int prevStateCount; // Previous count of state changes before resetting to 0;

// Constants
#define sensorInput D1 // The input that has a sensor to detect event; note:  for UNO, must be pin 2 or 3
#define enableDebug true // If printing debug info to serial
#define ONE_DAY_MILLIS (24 * 60 * 60 * 1000) // Number of milliseconds in a day

void setup() {
  // If debug mode enable, setup serial
  if(enableDebug) {
    Serial.begin(9600);
  }

  // Setup input mode for pullup of hall sensor
  pinMode(sensorInput, INPUT);

  // Setup interrupt to sensor pin when event is finishing (has dropped ping low, then rising back)
  attachInterrupt(sensorInput, sensorStateChange, RISING);

  // initialize variables
  stateCount = 0;
  startTime = micros();
  stopTime = micros();
}

void loop() {
  // Wait 60 seconds
  delay(60000);

  // If debug enabled, print some info to serial
  if(enableDebug) {
    printDebug();
  }
  // If clock hasn't been sync in over a day
  if (millis() - lastSync > ONE_DAY_MILLIS) {
    // Request time synchronization from the Particle Cloud
    Particle.syncTime();
    lastSync = millis();
  }
  // if connected to particle cloud
  if (Particle.connected()){
    // Reset event count
    prevStateCount = stateCount;
    stateCount = 0;

    // Turn state count into string
    //String dataToCloud = String(prevStateCount);
    // Trigger the integration
    Particle.publish("treadmill_stats_update",String(prevStateCount), PRIVATE);
  }
}

void sensorStateChange () {
  stateCount += 1;
  if(enableDebug) {
    Serial.println("Interrupted!");
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
