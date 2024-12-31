import numpy as np
import argparse
import cv2
import os

def process_video(video_path, prototxt, model, confidence_threshold):
    # Class labels and random colors for bounding boxes
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "table", "charger", "keyboard", "mouse", "monitor"]
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

    # Load the pre-trained model
    print("[INFO] Loading model...")
    net = cv2.dnn.readNetFromCaffe(prototxt, model)

    # Check if video file exists
    if not os.path.exists(video_path):
        print(f"[ERROR] Video file does not exist: {video_path}")
        return

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print("[ERROR] Couldn't open video. Please check the file path.")
        return

    print("[INFO] Processing video. Press 'q' to quit.")
    # Loop over the video frames
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[INFO] End of video.")
            break  # Break if we can't read a frame

        # Get the dimensions of the frame
        (h, w) = frame.shape[:2]

        # Preprocess the frame to be compatible with the model
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

        # Pass the blob through the network and obtain the detections
        net.setInput(blob)
        detections = net.forward()

        # Loop over the detections
        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            # Filter out weak detections
            if confidence > confidence_threshold:
                idx = int(detections[0, 0, i, 1])
                if idx >= len(CLASSES):  # Handle invalid class IDs
                    print(f"[WARNING] Invalid class ID: {idx}")
                    continue
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # Draw the bounding box and label on the frame
                label = f"{CLASSES[idx]}: {confidence * 100:.2f}%"
                cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

        # Show the output frame
        cv2.imshow("Output", frame)

        # Break the loop if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Video processing stopped by user.")
            break
         # Detect if the window is closed
        if cv2.getWindowProperty("Output", cv2.WND_PROP_VISIBLE) < 1:
            print("[INFO] Video window closed.")
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Argument parsing for model, confidence level, and video path
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--prototxt', default='model/MobileNetSSD_deploy.prototxt', help='Path to Caffe deploy prototxt file')
    ap.add_argument('-m', '--model', default='model/MobileNetSSD_deploy.caffemodel', help='Path to the Caffe pre-trained model')
    ap.add_argument('-c', '--confidence', type=float, default=0.2, help='Minimum probability to filter weak detections')
    ap.add_argument('-v', '--video', default='videos/sample_video.mp4', help='Path to input video')
    args = vars(ap.parse_args())

    # Run the video processing function
    process_video(args['video'], args['prototxt'], args['model'], args['confidence'])
