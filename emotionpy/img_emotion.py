import cv2
from deepface import DeepFace
import os
import argparse

def analyze_image(image_path):
    # Load face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Check if image exists and load it
    if not os.path.exists(image_path):
        print(f"[ERROR] Image file does not exist: {image_path}")
        return

    image = cv2.imread(image_path)
    if image is None:
        print("[ERROR] Could not load the image. Please check the file path.")
        return

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = image[y:y + h, x:x + w]

        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']

        # Draw rectangle around face and label with predicted emotion
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Show the output image
    print("[INFO] Press any key to close the output window.")
    cv2.imshow("Image Emotion Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Argument parsing for image path
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', default='samples/sample1.jpg', help='Path to the input image')
    args = vars(ap.parse_args())

    # Run the main function with the given or default image path
    analyze_image(args['image'])
