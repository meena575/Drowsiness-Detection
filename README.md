# Drowsiness Detection System

## Overview

This project implements a **Drowsiness Detection System** using a Convolutional Neural Network (CNN) model to detect if the driver's eyes are closed or open in real-time. The system uses a webcam to capture video frames and analyzes them to check for signs of drowsiness. If both eyes are detected as closed for a prolonged period, an alarm is triggered to alert the driver.

![Drowsiness Detection](https://cdn.hashnode.com/res/hashnode/image/upload/v1668417910288/bFctgCHVj.jpg)

## Features

- **Real-time drowsiness detection** using a pre-trained CNN model.
- **Alarm system** that triggers when drowsiness is detected (eyes closed for an extended period).
- **Webcam integration** to capture video frames for processing.
- **Streamlit web app** interface for easy usage.
  
## Technologies Used

- **OpenCV**: For video capture and image processing.
- **Keras**: For loading the pre-trained CNN model.
- **NumPy**: For efficient data manipulation.
- **Streamlit**: To build the web application interface.
- **Pygame**: For playing the alarm sound.
- **WebRTC**: For live streaming video capture via webcam.

## How it Works

1. **Webcam Capture**: The system captures video frames in real-time from the webcam using OpenCV.
2. **Face & Eye Detection**: Haar cascades are used to detect the driver's face, left eye, and right eye.
3. **Eye Classification**: A pre-trained CNN model classifies the state of the eyes (open or closed).
4. **Score Tracking**: The system maintains a score that increases if the eyes are closed and decreases if they are open.
5. **Alarm Trigger**: If the score exceeds a threshold, indicating that the driver's eyes have been closed for too long, an alarm sound is played to alert the driver.

## Setup and Installation

To run this project on your local machine, follow the steps below:

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)
  
### Dependencies

Install the required packages by running the following command:

```bash
pip install -r requirements.txt
Contents of requirements.txt:

Copy code
opencv-python
numpy
keras
streamlit
pygame
streamlit-webrtc
Clone the Repository
bash
Copy code
git clone https://github.com/meena575/Drowsiness-Detection.git
cd Drowsiness-Detection
Run the Application
To start the Streamlit web app, run the following command:

bash
Copy code
streamlit run app.py
This will open a browser window displaying the application. The app will start capturing video from your webcam for drowsiness detection.

File Structure
plaintext
Copy code
.
├── app.py                   # Main Streamlit app file
├── models
│   └── cnncat2.h5            # Pre-trained CNN model
├── haar cascade files
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_lefteye_2splits.xml
│   └── haarcascade_righteye_2splits.xml
├── alarm.wav                 # Alarm sound file
└── README.md                 # Project documentation
How to Use
Launch the Streamlit app.
Ensure your webcam is enabled and positioned properly to capture your face.
The system will display a live video feed and track your eye movements in real-time.
If the system detects that your eyes are closed for a prolonged period, it will trigger an audible alarm.
Model Information
The CNN model used in this project is pre-trained to classify images of eyes into two categories:

Open: Indicates the driver's eyes are open.
Closed: Indicates the driver's eyes are closed.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
OpenCV
Streamlit
Keras
