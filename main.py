### Psuedo code for now




### Initial test of inputs/outputs


### inputs
inputMotionSensor
inputPauseButton

### outputs
ledPersonPresent
ledQtrMile

# Loop
  # Check if person present
  if (person_present) {
    ledPersonPresent = On
  } else {
    ledPersonPresent = Off
  }

  # Assumption - flywheel = 13.5" from my measurements
  # 5280ft / 13.5" = 4,693 flywheel rotations
  # To test, but something on deck, turn flywheel, measure distance item moved on deck




# End Loop

function isPersonPresent () {
  # Check if person person
  if GPIO.input(inputMotionSensor) {
    return true;
  } else {
    return false;
  }

}
