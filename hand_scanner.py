import cv2
import mediapipe as mp
import numpy as np
import webbrowser
import tkinter as tk
from threading import Thread
import time
import pyautogui

# Load transparent hand template image
template = cv2.imread('hand_template.png', cv2.IMREAD_UNCHANGED)
template_h, template_w = template.shape[:2]

# Initialize MediaPipe for hand detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Draw transparent template on webcam feed
def overlay_image_alpha(img, img_overlay, pos):
    x, y = pos
    h, w = img_overlay.shape[:2]
    if x + w > img.shape[1] or y + h > img.shape[0]:
        return
    alpha = img_overlay[:, :, 3] / 255.0
    for c in range(3):
        img[y:y+h, x:x+w, c] = (
            alpha * img_overlay[:, :, c] +
            (1 - alpha) * img[y:y+h, x:x+w, c]
        )

# Show popup to trigger second scan
def show_second_popup(start_second_scan_callback):
    def on_click():
        popup.destroy()
        start_second_scan_callback()

    popup = tk.Tk()
    popup.title("Start Music")
    popup.geometry("300x150")
    label = tk.Label(popup, text="Scan hand to start music", font=("Arial", 12))
    label.pack(pady=20)
    button = tk.Button(popup, text="Start Hand Scanner Again", command=on_click)
    button.pack()
    popup.mainloop()

# Final popup to close the YouTube tab
def show_close_popup():
    def on_close():
        pyautogui.hotkey('ctrl', 'w')  # Closes browser tab
        root.destroy()

    root = tk.Tk()
    root.title("Close Video")
    root.geometry("250x100")
    label = tk.Label(root, text="🎵 Video is playing!")
    label.pack(pady=10)
    close_btn = tk.Button(root, text="❌ Close Video", command=on_close)
    close_btn.pack()
    root.mainloop()

# Second scan to start the music
def start_second_hand_scan():
    cap = cv2.VideoCapture(0)
    matched = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        center_x, center_y = w // 2 - template_w // 2, h // 2 - template_h // 2
        overlay_image_alpha(frame, template, (center_x, center_y))

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                x_coords = [lm.x for lm in hand_landmarks.landmark]
                y_coords = [lm.y for lm in hand_landmarks.landmark]
                x_min, x_max = int(min(x_coords) * w), int(max(x_coords) * w)
                y_min, y_max = int(min(y_coords) * h), int(max(y_coords) * h)

                if (center_x < x_min < center_x + template_w and
                    center_y < y_min < center_y + template_h and
                    center_x < x_max < center_x + template_w and
                    center_y < y_max < center_y + template_h):
                    matched = True
                    break

        if matched:
            print("✅ Second Scan Successful! Starting Music...")
            pyautogui.press('k')  # Presses 'k' to start video
            Thread(target=show_close_popup).start()
            break

        cv2.imshow("Scan Hand to Start Music", frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Initial scan to show "Scanning Successful" and open YouTube
def start_first_hand_scan():
    cap = cv2.VideoCapture(0)
    matched = False
    show_text = False
    text_time = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        center_x = w // 2 - template_w // 2
        center_y = h // 2 - template_h // 2

        overlay_image_alpha(frame, template, (center_x, center_y))
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if not matched and results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                x_coords = [lm.x for lm in hand_landmarks.landmark]
                y_coords = [lm.y for lm in hand_landmarks.landmark]
                x_min, x_max = int(min(x_coords) * w), int(max(x_coords) * w)
                y_min, y_max = int(min(y_coords) * h), int(max(y_coords) * h)

                if (center_x < x_min < center_x + template_w and
                    center_y < y_min < center_y + template_h and
                    center_x < x_max < center_x + template_w and
                    center_y < y_max < center_y + template_h):
                    matched = True
                    show_text = True
                    text_time = time.time()
                    webbrowser.open("https://youtu.be/eFDZOoVB2Ek?si=aFJKR3IcQ5TGxINz")  # 🔗 Replace link
                    Thread(target=show_second_popup, args=(start_second_hand_scan,)).start()
                    break

        # Show "Scanning Successful" for 2 seconds
        if show_text and time.time() - text_time < 2:
            cv2.putText(frame, "✅ Scanning Successful", (w//2 - 150, h//2),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        cv2.imshow("Initial Hand Scan", frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Start the complete program
start_first_hand_scan()
