# Fall Detection Research Summary

## Purpose
Before starting the sensor testing, I did some research on wearable fall detection.  
I wanted to understand the main types of falls, normal movements that could look similar to falls, and what data I should collect during testing.

## Sources Reviewed

1. **SisFall: A Fall and Movement Dataset** — Sucerquia et al. (2017)
  https://doi.org/10.3390/s17010198
2. **Elderly Fall Detection Systems: A Literature Survey** — Wang et al. (2020)
 https://doi.org/10.3389/frobt.2020.00071

## Key Findings

- Falls can happen in different directions, mainly forward, backward and lateral.
- Trips, slips and loss of balance are common causes of falls.
- Some normal movements can look similar to falls and may cause false alarms.
- Accelerometers are commonly used in wearable fall detection systems.
- Simulated falls may be different from real falls in older adults.

## Initial Testing Plan

Based on the research, I selected a small group of movements for the first testing stage.

### Fall-like movements

-  Forward fall-like movement
-  Backward fall-like movement
-  Lateral fall like movement
-  Trip-related movement
-  Sitting down or getting up movements

### Normal movements

- Walking slowly
- Walking quickly
- Sitting down and getting up quickly
- Bending down and getting up
- Stumbling while walking

## Next Step

The initial sensor testing will be done using the Raspberry Pi with the Sense HAT.
I will collect accelerometer and gyroscope data and compare the readings from different movements.
After that, the testing will move to the M5StickS3, which is the final wearable device for the project.
I have not selected the final fall detection method yet.
I want to look at the sensor data first and then decide which approach is most suitable.
