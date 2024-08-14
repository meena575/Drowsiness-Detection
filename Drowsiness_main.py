import cv2
import numpy as np
from keras.models import load_model
import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, RTCConfiguration
from pygame import mixer

# Initialize the mixer for playing alarm sound
mixer.init()
sound = mixer.Sound('alarm.wav')

class DrowsinessDetector(VideoTransformerBase):
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.face_cascade = cv2.CascadeClassifier('haar cascade files/haarcascade_frontalface_alt.xml')
        self.leye_cascade = cv2.CascadeClassifier('haar cascade files/haarcascade_lefteye_2splits.xml')
        self.reye_cascade = cv2.CascadeClassifier('haar cascade files/haarcascade_righteye_2splits.xml')
        self.lbl = ['Close', 'Open']
        self.score = 0
        self.thicc = 2
        self.count = 0

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        height, width = img.shape[:2]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = self.face_cascade.detectMultiScale(gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))
        left_eye = self.leye_cascade.detectMultiScale(gray)
        right_eye = self.reye_cascade.detectMultiScale(gray)

        cv2.rectangle(img, (0, height - 50), (200, height), (0, 0, 0), thickness=cv2.FILLED)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        rpred = lpred = 99  # Default values to avoid reference before assignment error

        for (x, y, w, h) in right_eye:
            r_eye = img[y:y+h, x:x+w]
            self.count += 1
            r_eye_gray = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
            r_eye_resized = cv2.resize(r_eye_gray, (24, 24))
            r_eye_normalized = r_eye_resized / 255.0
            r_eye_reshaped = np.reshape(r_eye_normalized, (1, 24, 24, 1))
            rpred_prob = self.model.predict(r_eye_reshaped)[0][0]  # Get the probability for class 0 (Closed)
            rpred = 0 if rpred_prob > 0.5 else 1  # Assign class based on threshold
            break

        for (x, y, w, h) in left_eye:
            l_eye = img[y:y+h, x:x+w]
            self.count += 1
            l_eye_gray = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
            l_eye_resized = cv2.resize(l_eye_gray, (24, 24))
            l_eye_normalized = l_eye_resized / 255.0
            l_eye_reshaped = np.reshape(l_eye_normalized, (1, 24, 24, 1))
            lpred_prob = self.model.predict(l_eye_reshaped)[0][0]  # Get the probability for class 0 (Closed)
            lpred = 0 if lpred_prob > 0.5 else 1  # Assign class based on threshold
            break

        if rpred == 0 and lpred == 0:  # Check if both eyes are closed
            self.score += 1
            cv2.putText(img, "Closed", (10, height - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, cv2.LINE_AA)
        else:
            self.score -= 1
            cv2.putText(img, "Open", (10, height - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, cv2.LINE_AA)

        if self.score < 0:
            self.score = 0

        cv2.putText(img, 'Score:' + str(self.score), (100, height - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
        if self.score > 15:
            cv2.imwrite('image.jpg', img)
            try:
                sound.play()
            except:
                pass
            if self.thicc < 16:
                self.thicc += 2
            else:
                self.thicc -= 2
                if self.thicc < 2:
                    self.thicc = 2
            cv2.rectangle(img, (0, 0), (width, height), (0, 0, 255), self.thicc)

        return img

RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

st.markdown("<h1 style='text-align: center;'>Drowsiness Detection</h1>", unsafe_allow_html=True)
image="https://cdn.hashnode.com/res/hashnode/image/upload/v1668417910288/bFctgCHVj.jpg"
st.markdown(
        f'<div style="text-align:center;">'
        f'<img src="{image}" style="width:100%;">'
        '</div>',
        unsafe_allow_html=True
        )
st.write("This application detects drowsiness in real-time using your webcam.")

webrtc_streamer(key="example", 
                rtc_configuration=RTC_CONFIGURATION,
                video_transformer_factory=lambda: DrowsinessDetector("models/cnncat2.h5"))
