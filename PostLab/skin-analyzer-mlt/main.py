import cv2
from utils.face_detect import detect_face
from utils.skin_analysis import analyze_skin

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = detect_face(frame)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]

        brightness, eye_darkness, acne = analyze_skin(face)

        # Suggestions
        text = []

        if eye_darkness < 80:
            text.append("Sleep more 😴")

        if brightness < 100:
            text.append("Drink water 💧")

        if acne > 500:
            text.append("Skin care needed 🧴")

        # Draw box
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        # Show suggestions
        y_offset = y - 10
        for t in text:
            cv2.putText(frame, t, (x, y_offset),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 2)
            y_offset -= 20

    cv2.imshow("Skin Analyzer", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()