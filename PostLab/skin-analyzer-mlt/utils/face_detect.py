import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection()

def detect_face(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb)

    faces = []
    if results.detections:
        for det in results.detections:
            bbox = det.location_data.relative_bounding_box
            h, w, _ = frame.shape

            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            w_box = int(bbox.width * w)
            h_box = int(bbox.height * h)

            faces.append((x, y, w_box, h_box))

    return faces