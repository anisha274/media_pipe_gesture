# Cargo Robot Vision: MediaPipe Hand Gesture Recognition Pipeline

Real-time hand gesture recognition system designed for autonomous cargo robots using Google MediaPipe Tasks Vision API and OpenCV.
This module allows a robot or automated system to process camera inputs in real time, evaluate human hand gestures, and trigger high-level operational commands (`STOP` vs `MOVE`).

https://github.com/user-attachments/assets/ab55961d-a682-420a-81d1-3fb7209399ab

## Features

- **Cross-Platform Compatibility:** Runs seamlessly on macOS (Apple Silicon / Intel), Linux, and Windows.
- **Low Latency Processing:** Built on MediaPipe Tasks Vision (`GestureRecognizer`), achieving real-time FPS on standard CPUs without requiring GPU acceleration.
- **Dynamic Robot State Mapping:**
  - `STOP`: Open Palm or Closed Fist (Emergency Hold).
  - `MOVE`: Pointing / Directional gestures (Resume Path Navigation).
- **Landmark Overlay:** Real-time visual tracking of 21 key hand joints over the camera feed.

## Prerequisites

- **Python 3.9+** installed on your system.
- A functional webcam or connected camera device.

## OS-Specific Testing Instructions
Follow the steps corresponding to your Operating System to set up and run the test.

###  macOS Setup & Testing

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/anisha274/media_pipe_gesture.git](https://github.com/anisha274/media_pipe_gesture.git)
   cd media_pipe_gesture

step-1: Download the MediaPipe Model File:
curl -O [https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task](https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task)

step-2: Virtual Environment & Dependencies:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

step-3:Run the Script:
python gesture_heuristics.py

macOS Permission Note: If prompted, grant camera permissions to VS Code or Terminal under System Settings > Privacy & Security > Camera.

🪟 Windows Setup & Testing
1.Clone the Repository (Command Prompt / PowerShell):
git clone [https://github.com/anisha274/media_pipe_gesture.git](https://github.com/anisha274/media_pipe_gesture.git)
cd media_pipe_gesture

2.Download the MediaPipe Model File (PowerShell):
Invoke-WebRequest -Uri "[https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task](https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task)" -OutFile "gesture_recognizer.task"

3.Virtual Environment & Dependencies:
 python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

4.Run the Script:
python gesture_heuristics.py

🐧 Linux (Ubuntu / Debian) Setup & Testing
1.Clone the Repository:
git clone [https://github.com/anisha274/media_pipe_gesture.git](https://github.com/anisha274/media_pipe_gesture.git)
cd media_pipe_gesture

2.Download the MediaPipe Model File:
curl -O [https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task](https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task)

3.Install OpenCV System Dependencies (If Needed):
sudo apt-get update && sudo apt-get install -y libgl1-mesa-glx python3-opencv

4.Virtual Environment & Dependencies:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

5.Run the Script:
python gesture_heuristics.py

How to Stop the Program
While the camera display window is active and focused, press 'q' on your keyboard to release the camera and exit cleanly.

License
Distributed under the MIT License. See LICENSE for more information.
