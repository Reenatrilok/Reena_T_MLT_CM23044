import cv2
import numpy as np

def analyze_skin(face_img):
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

    # Brightness check
    brightness = np.mean(gray)

    # Dark circle approx (lower region intensity)
    h, w = gray.shape
    eye_region = gray[int(h*0.6):int(h*0.8), int(w*0.2):int(w*0.8)]
    eye_darkness = np.mean(eye_region)

    # Simple acne detection (red spots)
    hsv = cv2.cvtColor(face_img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    acne_pixels = np.sum(mask > 0)

    return brightness, eye_darkness, acne_pixels