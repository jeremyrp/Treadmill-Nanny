# Treadmill-Nanny

## Overview
I use a treadmill desk, but find myself pausing/stopping it, yet forgetting to restart it.  I'm also not happy with the
metrics from the app, along with the PITA to sync over bluetooth.  So I want to constantly gather metrics, provide
a better dashboard for visualization and analysis of the metrics, and eventually drive feedback to improve (notify me
when I've been idle for too long, increase speed, etc...)

Components:
Hall Effect Sensor - to detect magnet on flywheel
Bracket to mount HE Sensor

Sensors
* Hall Effect (to count spins of flywheel)
* Motion detect (to tell that I'm standing there)

Buttons
* Sleep for xMin

LEDs
* Warning that detecting presense, but no activity
* Alert to start moving?

Thoughts
* Might need to use Arduinno to count flywheel steps
* Or build a step counter, which sounds too complicated

Crazy future
* graph activity throughout day (rrdtool?)
* Notify me to pickup pace
* Integrate with calendar to tell me when I need to "increase speed" based upon how I've categorized the meeting itself
