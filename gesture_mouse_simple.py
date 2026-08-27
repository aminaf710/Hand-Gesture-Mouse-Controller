import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# ----------------------------
# Setup Mediapipe Hands
# ----------------------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

prev_x, prev_y = 0, 0
smoothening = 7
click_flag = False

with mp_hands.Hands(min_detection_confidence=0.7,
                    min_tracking_confidence=0.7,
                    max_num_hands=1) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, c = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                landmarks = hand_landmarks.landmark

                # ----------------------------
                # Finger detection
                # ----------------------------

                # Thumb
                thumb_down = landmarks[4].x > landmarks[3].x

                # Index finger
                index_up = landmarks[8].y < landmarks[6].y

                # Middle finger
                middle_down = landmarks[12].y > landmarks[10].y

                # Ring finger
                ring_down = landmarks[16].y > landmarks[14].y

                # Pinky finger
                pinky_up = landmarks[20].y < landmarks[18].y

                # ----------------------------
                # Move the mouse only when
                # the index finger and pinky are up
                # ----------------------------
                if index_up and pinky_up and thumb_down and middle_down and ring_down:

                    margin_x = int(w * 0.2)
                    margin_y = int(h * 0.2)

                    x = np.clip(
                        landmarks[8].x * w,
                        margin_x,
                        w - margin_x
                    )

                    y = np.clip(
                        landmarks[8].y * h,
                        margin_y,
                        h - margin_y
                    )

                    # Convert to screen coordinates
                    screen_x = np.interp(
                        x,
                        (margin_x, w - margin_x),
                        (0, screen_w)
                    )

                    screen_y = np.interp(
                        y,
                        (margin_y, h - margin_y),
                        (0, screen_h)
                    )

                    # Smooth mouse movement
                    curr_x = prev_x + (screen_x - prev_x) / smoothening
                    curr_y = prev_y + (screen_y - prev_y) / smoothening

                    pyautogui.moveTo(curr_x, curr_y)

                    prev_x, prev_y = curr_x, curr_y

                # ----------------------------
                # Detect double click
                # (thumb touching pinky)
                # ----------------------------
                x1, y1 = int(landmarks[4].x * w), int(landmarks[4].y * h)   # Thumb
                x2, y2 = int(landmarks[20].x * w), int(landmarks[20].y * h) # Pinky

                distance = np.hypot(x2 - x1, y2 - y1)

                if distance < 40:  # Distance threshold
                    if not click_flag:
                        pyautogui.doubleClick()
                        click_flag = True

                        cv2.putText(
                            frame,
                            "Double Click",
                            (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2
                        )
                else:
                    click_flag = False

        cv2.imshow("Gesture Mouse", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
