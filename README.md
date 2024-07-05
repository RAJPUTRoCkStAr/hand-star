# HandStar

HandStar is a Python library that uses Mediapipe and OpenCV to make hand detection and tracking easy. It provides functionalities to detect hands in real-time from camera feed, visualize hand landmarks, and calculate distances between specific landmarks.

## Features

- Real-time hand detection and tracking.
- Visualization of hand landmarks and connections.
- Calculation of distances between specified landmarks (e.g., fingertips).

## Installation

You can install HandStar using pip:

```bash
pip install hand-star
```
## Code
```bash
import cv2
from hand_star.hand_star import HandStar

def main():
    cap = cv2.VideoCapture(0)
    detector = HandStar(maxHands=2)

    while True:
        success, img = cap.read()
        if not success:
            break
        
        img = detector.detect_hands(img)
        lmList = detector.get_hand_positions(img)
        
        # Additional functionalities
        fingersList = detector.get_fingers_status()
        for i, fingers in enumerate(fingersList):
           print(f"Hand {i+1}:", fingers)
            length, img, lineInfo = detector.calculate_distance(4, 8, img, handNo=i)
            print(f"Hand {i+1} Distance:", length)
        
        cv2.imshow('Hand Detection', img)
        
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

```

## Contact
For any questions or feedback, feel free to reach out at [sumitsingh9441@gmail.com](mailto:sumitsingh9441@gmail.com).
