import cv2
# import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands model
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1)

# Set up volume control
def decrease_volume():
    volume = np.array([cv2.getWindowProperty('Gestro', cv2.WND_PROP_VOLUME)], dtype=np.float32)
    cv2.setWindowProperty('Gestro', cv2.WND_PROP_VOLUME, max(0, volume - 10))

def increase_volume():
    volume = np.array([cv2.getWindowProperty('Gestro', cv2.WND_PROP_VOLUME)], dtype=np.float32)
    cv2.setWindowProperty('Gestro', cv2.WND_PROP_VOLUME, min(100, volume + 10))

# Process the video frame
def process_frame(frame):
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the landmarks
            landmarks = hand_landmarks.landmark

            # Extract the pointing finger tips
            left_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP.value]
            right_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP.value]

            # Calculate the angle between the fingers
            angle = np.arctan2(right_tip.y - left_tip.y, right_tip.x - left_tip.x)

            # Check the gesture
            if angle > 0:
                increase_volume()
            else:
                decrease_volume()

            # Draw the hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

# Start the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    process_frame(frame)

    cv2.imshow('Gestro', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the windows
cap.release()
cv2.destroyAllWindows()