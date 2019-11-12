import cv2
import os
import numpy as np
import pyttsx3
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "invicta",
    passwd = "DRAGONBALL",
    database = "names",
    port = "3300"
    )
mycursor = mydb.cursor()
engine = pyttsx3.init()
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX

#id=0
#names=['NONE','MARCELO','PAULA','ILZA','Z','W']
cam =cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW),int(minH)),)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        if (confidence<100):
            id = id
            confidence="{0}%".format(round(100-confidence))
        else:
            id="unknown"
            confidence = "{0}%".format(round(100-confidence))
        try:
            sql = "select name from NAMES where ids=%s" %(id)
            mycursor.execute(sql)
            a = mycursor.fetchone()
            mydb.commit()
            O=str(a[0])
        except mysql.connector.Error as error:
            O=str("UNKNOWN")
        cv2.putText(
            img,
            str(str(id)+" "+O),
            (x+5,y-5),
            font,
            1,
            (255,255,255,255),
            2
            )
        cv2.putText(
            img,
            str(confidence),
            (x+5,y+h-5),
            font,
            1,
            (255,255,0),
            1
            )
        speak = "suspect "+str(O)+" having id number "+str(id)+" with confidence level "+str(confidence)
        print(speak)
        engine.say(speak)
        engine.setProperty('rate',120)
        engine.setProperty('volume',1.0)
        engine.runAndWait()
        
    cv2.imshow('camera',img)
    k=cv2.waitKey(10) &0xff
    if k==27:
        break
print("wait")
cam.release()
cv2.destroyAllWindows()
