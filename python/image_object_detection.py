import numpy as np
import argparse
import cv2
import os

def main(image_path, prototxt, model, confidence_threshold):
    # Class labels and colors
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "table", "charger", "keyboard", "mouse", "monitor"]
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

    # Load the pre-trained model
    print("[INFO] Loading model...")
    net = cv2.dnn.readNetFromCaffe(prototxt, model)

    # Check if image exists and load it
    if not os.path.exists(image_path):
        print(f"[ERROR] Image file does not exist: {image_path}")
        return

    image = cv2.imread(image_path)
    if image is None:
        print("[ERROR] Could not load the image. Please check the file path.")
        return

    # Resize image to 300x300 for the model
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    # Pass the blob through the network and obtain the detections and predictions
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

            # Draw the prediction on the image
            label = f"{CLASSES[idx]}: {confidence * 100:.2f}%"
            cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    # Show the output image
    print("[INFO] Press any key to close the output window.")
    cv2.imshow("Output", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Argument parsing for model, confidence level, and image path
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--prototxt', default='model/MobileNetSSD_deploy.prototxt', help='Path to Caffe deploy prototxt file')
    ap.add_argument('-m', '--model', default='model/MobileNetSSD_deploy.caffemodel', help='Path to the Caffe pre-trained model')
    ap.add_argument('-c', '--confidence', type=float, default=0.2, help='Minimum probability to filter weak detections')
    ap.add_argument('-i', '--image', default='images/sample.jpg', help='Path to the input image')
    args = vars(ap.parse_args())

    # Run the main function
    main(args['image'], args['prototxt'], args['model'], args['confidence'])
