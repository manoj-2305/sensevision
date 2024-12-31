from imutils.video import VideoStream, FPS
import numpy as np
import argparse
import imutils
import time
import cv2

# Argument parsing
ap = argparse.ArgumentParser()
ap.add_argument('-p', '--prototxt', default='model/MobileNetSSD_deploy.prototxt', help='Path to Caffe deploy prototxt file')
ap.add_argument('-m', '--model', default='model/MobileNetSSD_deploy.caffemodel', help='Path to the Caffe pre-trained model')
ap.add_argument('-c', '--confidence', type=float, default=0.2, help='Minimum probability to filter weak detections')
args = vars(ap.parse_args())

# Class labels and random colors for bounding boxes
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "table", "charger", "keyboard", "mouse", "monitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# Load the serialized model from disk
print("[INFO] Loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# Initialize the video stream, allow the camera to warm up, and initialize the FPS counter
print("[INFO] Starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()

try:
    # Loop over the frames from the video stream
    while True:
        # Grab the frame from the video stream and resize it
        frame = vs.read()
        frame = imutils.resize(frame, width=800, height=600)

        # Grab the frame dimensions and convert it to a blob
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

        # Pass the blob through the network and obtain detections and predictions
        net.setInput(blob)
        detections = net.forward()

        # Loop over the detections
        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            # Filter out weak detections
            if confidence > args["confidence"]:
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # Draw the prediction on the frame
                label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

        # Show the output frame
        cv2.imshow("Frame", frame)
        

        # Check if the `x` key was pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord("x"):
            print("[INFO] 'x' key pressed, closing...")
            break

        # Check if the window was closed manually
        
        if cv2.getWindowProperty("Frame", cv2.WND_PROP_AUTOSIZE) < 0:
            print("[INFO] Window closed manually, exiting...")
            break

        # Update the FPS counter
        fps.update()

except KeyboardInterrupt:
    print("[INFO] Exiting due to keyboard interrupt...")

# Stop the timer and display FPS information
fps.stop()
print("[INFO] Elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] Approx. FPS: {:.2f}".format(fps.fps()))

# Clean up
cv2.destroyAllWindows()
vs.stop()
