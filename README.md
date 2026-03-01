# 🚗 Real-Time Speed Detection using OpenCV

A Python-based real-time speed detection system that uses optical flow analysis via your webcam to detect fast-moving objects. When the detected speed exceeds a defined threshold, the system flags it as **overspeeding** and automatically saves a screenshot.

---

## 📸 How It Works

The program captures live video from your webcam and uses **Farneback Optical Flow** to estimate motion between consecutive frames. The magnitude of the optical flow vectors is used as a proxy for speed. If the calculated speed exceeds the threshold, an alert is displayed on screen and a screenshot is saved locally.

---

## 🛠️ Requirements

- Python 3.x
- OpenCV

Install the dependency with:

```bash
pip install opencv-python
```

---

## 🚀 Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/speed-detection.git
cd speed-detection
```

2. Run the script:

```bash
python speed_detection.py
```

3. A window will open showing your webcam feed. Move an object quickly in front of the camera to trigger the overspeeding alert.

4. Press **`q`** to quit the application.

---

## ⚙️ Configuration

You can adjust the following variable in the script to tune sensitivity:

| Variable           | Default | Description                                              |
|--------------------|---------|----------------------------------------------------------|
| `speed_threshold`  | `25`    | The speed value above which overspeeding is triggered    |

Lowering the threshold makes the detection more sensitive; raising it requires faster movement to trigger an alert.

---

## 📂 Output

When overspeeding is detected, screenshots are automatically saved in the project directory with filenames like:

```
screenshot_1.png
screenshot_2.png
...
```

---

## 📋 Features

- Real-time motion analysis using Farneback Optical Flow
- On-screen **"Overspeeding"** text alert in red when threshold is exceeded
- Automatic screenshot capture on detection
- Lightweight — runs entirely on CPU with a standard webcam

---

## ⚠️ Limitations

- Speed is estimated from optical flow magnitude and is a **relative measure**, not an absolute real-world speed (e.g., km/h or mph)
- Accuracy depends on camera quality, frame rate, and lighting conditions
- Designed for single-camera setups; not calibrated for real-world distance measurement

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
