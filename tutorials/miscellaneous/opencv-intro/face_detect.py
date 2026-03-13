# OpenCV Face Detection
# ---------------------
# Open Source Computer Vision Library (cv2) is the powerhouse of image processing.

import cv2

def detect_faces():
    # 1. Load the pre-trained Haar Cascade classifier for faces
    # This XML file contains the 'knowledge' of what a face looks like.
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 2. Access the Webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    print("Press 'q' to quit the camera view.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # 3. Pre-processing
        # OpenCV works better on grayscale images for detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 4. Detection
        # detectMultiScale returns coordinates (x, y, w, h) for detected faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # 5. Drawing Rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Blue box, thickness 2
            cv2.putText(frame, 'Face Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # 6. Display the resulting frame
        cv2.imshow('Face Detection Demo', frame)

        # Exit loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # This will attempt to open your webcam. Ensure no other app is using it.
    try:
        detect_faces()
    except Exception as e:
        print(f"Error accessing camera: {e}")