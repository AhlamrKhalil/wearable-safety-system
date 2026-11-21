# Development Log - Wearable Safety System

This log records my weekly progress, decisions, tests and problems during development.

---

## Week 1: 15-21 Nov 2026

### Activities
- **15 Nov:** Designed the system architecture diagram in draw.io.
- **15 Nov:** Made a graph of the Sense HAT accelerometer data, updated the README and merged into main (PR #2).
- **16 Nov:** Prepared the Demo 1 presentation (motivation, background research, architecture, first results and timeline).
- **17 Nov:** Merged the new README into main (PR #3) and made the repo public so my supervisor and second reader can see it.
- **20 Nov:** Presented Demo 1 online on Teams.
- **20 Nov:** Fixed a connection problem with the M5StickS3 and set it up again.
- **20 Nov:** Looked at different ways to program the M5StickS3 and chose my development environment.
- **21 Nov:** Went through the final report requirements and started this development log.

### Decisions
- I will use MicroPython on the M5StickS3 and write the code in VS Code, so all my code is in GitHub.

### Tests and Results
- No tests this week.

### Problems and Solutions
- **Problem:** The M5StickS3 screen stayed black and it would not connect.
  **Solution:** I found the port had changed from COM5 to COM4, then set the device up again with M5Burner.
- **Demo 1 feedback:** I was advised to clearly define which ML model I will use. Next step is to research and choose an ML approach.

### Next
- Connect VS Code to the M5StickS3
- Research ML models for fall detection

---

## Before Week 1: Oct - 14 Nov 2026 (summary)

### Activities
- **Oct - Nov:** Researched fall detection (accelerometers, gyroscopes, fall types, false alarms) and read papers including SisFall and Wang et al.
- **8 Nov:** Installed UIFlow2 on the M5StickS3 and tested the accelerometer and gyroscope readings.
- **14 Nov:** Recorded movement data with the Raspberry Pi and Sense HAT and saved it to a CSV file. Merged my first work into main (PR #1).