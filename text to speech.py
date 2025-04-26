import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import pyttsx3
import time
import serial
import keyboard

# replace the url with your esp32 cma stream server url
url = 'http://192.168.209.119:81/stream'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def text_to_speech(label):
    engine = pyttsx3.init()
    engine.say(label)
    engine.runAndWait()

start_time = None



while True:
    button_state = 0
    ret, frame = cap.read()
    cv2.imshow('Frame', frame)
    
   
        
    if keyboard.is_pressed("1"):
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        

        bbox, label, conf = cv.detect_common_objects(frame)
        
        for i in range(len(label)):

            # Trigger text-to-speech for the largest object's label
            text_to_speech(label[i])
            
# Break the loop 
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()


