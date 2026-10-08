import cv2
import time
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

def main():
    # 1. Initialize MediaPipe Gesture Recognizer
    model_path = "gesture_recognizer.task"
    
    base_options = python.BaseOptions(model_asset_path=model_path)
    options = vision.GestureRecognizerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.LIVE_STREAM,
        num_hands=1,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        result_callback=lambda result, output_image, timestamp_ms: None
    )
    
    # Store dynamic result in container
    latest_result = {"gesture": "SEARCHING...", "landmarks": None}

    def result_callback(result, output_image, timestamp_ms):
        if result.gestures and len(result.gestures) > 0:
            gesture_name = result.gestures[0][0].category_name
            
            # Map built-in gestures or defaults
            if gesture_name in ["Open_Palm", "Closed_Fist"]:
                latest_result["gesture"] = "STOP"
            elif gesture_name in ["Pointing_Up", "Victory", "Thumb_Up"]:
                latest_result["gesture"] = "MOVE"
            else:
                latest_result["gesture"] = f"GESTURE: {gesture_name}"
                
            if result.hand_landmarks:
                latest_result["landmarks"] = result.hand_landmarks[0]
        else:
            latest_result["gesture"] = "SEARCHING..."
            latest_result["landmarks"] = None

    options.result_callback = result_callback
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("[INFO] Starting MediaPipe Gesture Recognizer...")
    
    with vision.GestureRecognizer.create_from_options(options) as recognizer:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            
            # Convert frame format
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            
            frame_timestamp_ms = int(time.time() * 1000)
            recognizer.recognize_async(mp_image, frame_timestamp_ms)

            # Draw Hand Landmarks manually if available
            if latest_result["landmarks"]:
                for lm in latest_result["landmarks"]:
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(frame, (cx, cy), 4, (0, 255, 0), -1)

            # Set text colors based on gesture status
            status = latest_result["gesture"]
            if status == "STOP":
                color = (0, 0, 255) # Red
            elif status == "MOVE":
                color = (0, 255, 0) # Green
            else:
                color = (0, 255, 255) # Yellow

            cv2.putText(frame, f"ROBOT STATE: {status}", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2, cv2.LINE_AA)

            cv2.imshow("Robot Gesture Interface", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()