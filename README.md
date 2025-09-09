# ✋ Hand Gesture Mouse Controller

Control your computer mouse in real-time using **hand gestures** with **Mediapipe**, **OpenCV**, and **PyAutoGUI**.
Move your cursor, smooth the movement, and perform **double-clicks** without touching your mouse.

---

## 📂 Project Structure

```
gesture-mouse/
│
├── gesture_mouse.py       # Main hand gesture mouse script
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## ⚙️ Installation

1. Install Python dependencies:

```bash
pip install opencv-python mediapipe pyautogui numpy
```

2. Optional: Use a **CUDA-enabled GPU** if OpenCV supports it for faster webcam processing.

---

## ▶️ Usage

1. Connect your webcam and run the script:

```bash
python gesture_mouse.py
```

2. Gestures:

* **Move cursor** → Raise **index + pinky** finger, keep others down
* **Double-click** → Bring **thumb** close to **pinky**
* **Exit** → Press `ESC`

3. Optional configurable settings inside `gesture_mouse.py`:

* `MARGIN_RATIO` → Defines safe margin inside camera frame
* `SMOOTHENING` → Smoothness of mouse movement (higher → smoother but slower)
* `CLICK_RATIO` → Sensitivity for double-click detection
* `INVERT_X` → Invert horizontal axis if needed
* `MIRROR` → Flip webcam feed if image appears mirrored

---

## 🧠 How It Works

1. **Hand Tracking**: Mediapipe detects hand landmarks in real-time.
2. **Finger State Detection**: Thumb, index, middle, ring, pinky fingers are monitored.
3. **Cursor Movement**: Maps index finger position from camera frame to screen coordinates.
4. **Smooth Movement**: Uses exponential moving average for natural cursor movement.
5. **Double-click Detection**: Based on distance between thumb and pinky.

---

## 📌 Notes & Tips

* Works best with **single hand** and **well-lit environment**.
* Recommended webcam: **30+ FPS** for smooth tracking.
* Adjust `smoothening` and `CLICK_RATIO` for personalized control.
* Make sure your screen resolution is detected correctly; it automatically adapts.


---

## 📦 Dependencies

```
opencv-python
mediapipe
pyautogui
numpy
```

---
