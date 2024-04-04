import cv2
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

# Initialize pycaw for volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get volume range
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

# Initialize OpenCV's optical flow algorithm
prev_gray = None

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Flip the frame horizontally for a more natural selfie-view
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Initialize the optical flow algorithm
    if prev_gray is None:
        prev_gray = gray
        continue

    # Calculate the optical flow
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Get the movement of the thumb and index finger
    thumb_tip = np.array([[landmarks[mp_hands.HandLandmark.THUMB_TIP.value].x, landmarks[mp_hands.HandLandmark.THUMB_TIP.value].y]])
    index_tip = np.array([[landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP.value].x, landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP.value].y]])
    thumb_index_diff = thumb_tip - index_tip

    # Calculate the angle between the thumb and index finger
    angle = np.arctan2(thumb_index_diff[0, 1], thumb_index_diff[0, 0]) * 180 / np.pi

    # Check if the hand is showing the "thumbs up" or "thumbs down" gesture
    if angle > 130 and angle < 160:
        # Increase the volume
        curVol = int(volume.GetMasterVolumeLevel() * 100 / (maxVol - minVol))
        vol = curVol + 1
        if vol > 100:
            vol = 100
        volume.SetMasterVolumeLevel((vol / 100) * (maxVol - minVol), None)
    elif angle < -130 and angle > -160:
        # Decrease the volume
        curVol = int(volume.GetMasterVolumeLevel() * 100 / (maxVol - minVol))
        vol = curVol - 1
        if vol < 0:
            vol = 0
        volume.SetMasterVolumeLevel((vol / 100) * (maxVol - minVol), None)

    # Draw the optical flow on the frame
    for i, j in zip(*np.where(np.abs(flow) > 1)):
        cv2.circle(frame, (i, j), 1, (0, 255, 0), -1)

    # Draw the thumb and index finger on the frame
    cv2.polylines(frame, [thumb_tip], True, (0, 255, 0), 5)
    cv2.polylines(frame, [index_tip], True, (0, 255, 0), 5)

    # Show the resulting image
    cv2.imshow('Hand Gesture Volume Control', frame)

    # Update the previous frame
    prev_gray = gray

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()