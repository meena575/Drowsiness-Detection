# Drowsiness Detection System
## Overview
This project is a real-time drowsiness detection application that monitors a driver's eye state using a webcam. It uses a pre-trained Convolutional Neural Network (CNN) to detect whether a person's eyes are open or closed and raises an alarm if the person shows signs of drowsiness.
![Drowsiness Detection](https://cdn.hashnode.com/res/hashnode/image/upload/v1668417910288/bFctgCHVj.jpg)
## Contents

1. [Features](#features)
2. [Demo](#demo)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [How to Run](#how-to-run)
6. [How It Works](#how-it-works)
7. [Folder Structure](#folder-structure)
8. [Usage Instructions](#usage-instructions)
9. [Contributing](#contributing)
10. [Acknowledgments](#acknowledgments)

## Features

- **Real-Time Detection**: Detects drowsiness through webcam feed using OpenCV and Keras.
- **Alarm System**: Plays an alarm sound when the driver is detected to be drowsy.
- **Eye State Analysis**: Analyzes both left and right eyes using Haar Cascade Classifiers.
- **Streamlit Web App**: Simple and interactive UI built with Streamlit for real-time monitoring.

## Project Demo

![Watch Here](https://drive.google.com/file/d/1xjETyxO0QwACW1p6WWKTXxhhQ_mXVJ-5/view?usp=sharing)
This application detects drowsiness in real-time using your webcam.

You can check out a live demo of the project by running the app on your local machine (instructions in the **How to Run** section).

## Requirements

To run this project, make sure you have the following dependencies installed:

- Python 3.x
- OpenCV (`opencv-python`)
- Keras
- TensorFlow
- NumPy
- Pygame
- Streamlit
- streamlit-webrtc

You can install these using the following command:

  ```bash
    pip install opencv-python keras tensorflow numpy pygame streamlit streamlit-webrtc
  ```
## Installation
1. **Clone the repository:**

  ```bash
    git clone https://github.com/your-username/drowsiness-detection.git
    cd drowsiness-detection
  ```

2. **Download the required pre-trained model:**
    - **Pre-trained Models**
  
      The required pre-trained model for drowsiness detection can be found in the `models/` folder of this 
      repository. You can download the model file from the following link:
      - [Download cnncat2.h5](models/cnncat2.h5)
    - **Haar Cascade Files**
  
      The Haar Cascade XML files required for face and eye detection can be found in the `haar cascade files/`     
      folder in this repository. You can download them from the following links:
  
      - [Download haarcascade_frontalface_alt.xml](haar%20cascade%20files/haarcascade_frontalface_alt.xml)
      - [Download haarcascade_lefteye_2splits.xml](haar%20cascade%20files/haarcascade_lefteye_2splits.xml)
      - [Download haarcascade_righteye_2splits.xml](haar%20cascade%20files/haarcascade_righteye_2splits.xml)
3. **Run the Streamlit app:**

    ```bash
      streamlit run app.py
    ```
The app will launch in your default browser, and you can begin real-time drowsiness detection via your webcam.

## How It Works
1. **Face and Eye Detection:**

 - The app uses Haar Cascade Classifiers to detect faces, left eye, and right eye in the webcam feed.
2. **CNN Model:**

  - A CNN model is used to classify whether the eyes are open or closed based on the eye regions extracted from      the webcam feed.
3. **Drowsiness Score:**

  - The app continuously monitors the eye state. If both eyes are closed for a certain period (a score of 15),       it triggers an alarm sound to alert the driver.
## Folder Structure
  ```bash
    
    ├── app.py                     # Main application file
    ├── models/
    │   └── cnncat2.h5             # Pre-trained CNN model
    ├── haar cascade files/
    │   ├── haarcascade_frontalface_alt.xml      # Haar Cascade for face detection
    │   ├── haarcascade_lefteye_2splits.xml      # Haar Cascade for left eye detection
    │   └── haarcascade_righteye_2splits.xml     # Haar Cascade for right eye detection
    ├── alarm.wav                  # Alarm sound file
    ├── README.md                  # Project documentation
```
## Usage Instructions
  - Once the app is running, allow access to your webcam.
  - The app will display the webcam feed, along with eye status (Open/Closed) and a drowsiness score.
  - If drowsiness is detected, an alarm will sound to wake up the driver.
## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

## Acknowledgments
  - Haar Cascades are provided by OpenCV.
  - CNN model for eye detection was trained using Keras and TensorFlow.
