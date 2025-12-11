This project uses OpenCV's Farneback Optical Flow algorithm to estimate movement between video frames, convert the motion into approximate real-world speed, and automatically trigger an alert when an object exceeds the configured speed limit.
It can capture screenshots of overspeed events and works on any webcam or CCTV feed.

Features

Real-time video processing
Optical Flow-based motion tracking
Speed calculation in meters per second
Overspeed detection above 25 m/s (90 km/h)
Automatic screenshot capture upon violation
Clean on-screen overlays (speed + warnings)
Works with live camera or video file


If speed > 25 m/s:
Display “OVERSPEEDING” on screen
Save a screenshot
Print an alert message in terminal
