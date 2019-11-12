'''import cgitb cgitb.enable()
start_response('200 OK',[('Content-Type','text/html')])'''

import cv2
import os
import mysql.connector
import speech_recognition as sr
mydb = mysql.connector.connect(
    host = "localhost",
    user = "invicta",
    passwd = "DRAGONBALL",
    database = "names",
    port = "3300"
    )
mycursor = mydb.cursor()
r = sr.Recognizer()
mic = sr.Microphone(device_index = 0)
cam = cv2.VideoCapture(0)
cam .set(3,640)
cam.set(4,480)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
with mic as source:
    print("what is subject name - >")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    sql = "INSERT INTO NAMES (name) VALUE ('%s')" %(r.recognize_google(audio))
    #print(sql)
    mycursor.execute(sql)
    mydb.commit()
    
face_id = mycursor.lastrowid;    
#l = input('\n enter user id and name, press <return> ==> ').split()
#face_id =  l[0]
print("\n [INFO] Intializing face capture. Look the camera and wait ...")
count = 0
while(True):
    res, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        count+=1
        cv2.imwrite("dataset/User"+"."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
        #cv2.imwrite("file://192.168.42.230/ImageData/User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
        

        cv2.imshow('image',img)
    k=cv2.waitKey(100) & 0xff
    if k==27:
        break
    elif count >=30:
        break
print("\n [INFO] Exciting Program and Cleanup stuff")
cam.release()
cv2.destroyAllWindows()
