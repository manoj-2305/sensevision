import cv2
from deepface import DeepFace
import argparse

def analyze_video(video_path):
    # Load face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"[ERROR] Could not open video file: {video_path}")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("[INFO] End of video file.")
            break

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Extract the face ROI (Region of Interest)
            face_roi = frame[y:y + h, x:x + w]

            # Perform emotion analysis on the face ROI
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

            # Determine the dominant emotion
            emotion = result[0]['dominant_emotion']

            # Draw rectangle around face and label with predicted emotion
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # Display the resulting frame
        cv2.imshow("Video Emotion Detection", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("x"):
            print("[INFO] 'x' key pressed, closing...")
            break

        # Check if the window was closed manually
        if cv2.getWindowProperty("Video Emotion Detection", cv2.WND_PROP_AUTOSIZE) < 0:
            print("[INFO] Window closed manually, exiting...")
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Argument parsing for video path
    ap = argparse.ArgumentParser()
    ap.add_argument('-v', '--video', default='samples/sample_video1.mp4', help='Path to the input video')
    args = vars(ap.parse_args())

    # Run the emotion analysis with the provided or default video path
    analyze_video(args['video'])
