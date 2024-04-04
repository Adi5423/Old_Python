import cv2
import numpy as np
import ctypes

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Initialize the OpenCV hand landmark model
hand_cascade = cv2.CascadeClassifier("haarcascade_hand.xml")

# Initialize audio volume
min_vol = 0
max_vol = 100
vol = min_vol

# Initialize audio device
device = ctypes.windll.winmm.waveOutGetDefaultDevice()

while True:
    # Read the frame
    ret, frame = cap.read()

    # Process the image with OpenCV
    hands = hand_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

    if hands:
        # Draw bounding boxes around the detected hands
        for hand in hands:
            x, y, w, h = hand
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Check for thumbs up gesture
            hand_roi = frame[y-10:y + h + 10, x-10:x + w + 10]
            fingers_open = 0

            for fingers in hand_roi:
                for finger in fingers:
                    fingers_open += (240 > finger[1])

            if fingers_open == 2:
                # Thumbs up gesture detected, increase volume
                if vol < max_vol:
                    vol += 1
            else:
                # Otherwise, decrease volume
                if vol > min_vol:
                    vol -= 1

            # Set the volume
            ctypes.windll.winmm.waveOutSetVolume(device, int(vol * 65536))

    # Display the frame
    cv2.imshow("Frame", frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()