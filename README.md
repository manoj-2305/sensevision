# Emotion and Object Detection Application

This project involves emotion recognition and object detection using Python and PHP. The application leverages OpenCV for face detection, MobileNetSSD for object detection, and PHPMailer for email functionalities.

## Setup Instructions

### 1. Create a Virtual Environment
To set up the environment for this project:

- Run the following command in the project directory:

  python -m venv .venv
Activate the virtual environment:

On Windows:


.venv\Scripts\activate
On macOS/Linux:


source .venv/bin/activate
2. Install Required Modules
Install all necessary Python modules using pip:


pip install opencv-python opencv-contrib-python numpy flask
3. Download Models
To use the face detection and object detection models:

Haar Cascade Model: Download the face detection model from OpenCV:

Download haarcascade_frontalface_default.xml
MobileNetSSD Models: Download the object detection models:

Download MobileNetSSD_deploy.caffemodel
Download MobileNetSSD_deploy.prototxt
Place the downloaded files in the model/ directory.

4. Download PHPMailer
Download the PHPMailer library from GitHub:

Download PHPMailer
Extract the library and place it in the PHPMailer/ directory.

5. Configure the Database
Open config.php and update it with your database credentials.
Run create_db.php to initialize the database structure.
6. Run the Application
Start the PHP backend server:


php -S localhost:8000
Run Python scripts for emotion and object detection:

python app.py
References
1. OpenCV Models:
Haarcascade Model for Face Detection: Link to Haarcascade
MobileNetSSD for Object Detection: Link to MobileNet-SSD
2. PHPMailer Library:
Official GitHub Repository
3. CustomTkinter Library:
Official Documentation and Resources
4. Books for Emotion and Object Detection:
"Deep Learning for Computer Vision" by Rajalingappaa Shanmugamani.
"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron.
5. Development Tools:
Visual Studio Code (VS Code)
Python
6. Additional Python Libraries:
NumPy
OpenCV Documentation
Requests Library for HTTP Requests
7. Emotion Detection Research:
"Emotion Recognition with Machine Learning" by Yann LeCun and Yoshua Bengio (Journal Articles).
"Facial Expression Recognition Using Deep Learning" (IEEE Conference Proceedings).
8. Object Detection Research:
"You Only Look Once (YOLO): Unified, Real-Time Object Detection" by Joseph Redmon.
"Faster R-CNN: Towards Real-Time Object Detection" by Shaoqing Ren et al.

This `README.md` provides the setup instructions and references for the project. You can us
