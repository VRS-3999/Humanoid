'''import cgitb cgitb.enable()
start_response('200 OK',[('Content-Type','text/html')])'''

import cv2
import os
from PIL import Image
#from io import StringIO
#from six import StringIO
#from io import BytesIO
import requests
#import numpy as np
#import base64


cam = cv2.VideoCapture(0)
cam .set(3,640)
cam.set(4,480)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('\n enter user id end press <return> ==> ')
print("\n [INFO] Intializing face capture. Look the camera and wait ...")
count = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        count+=1
        #cv2.imwrite("http://localhost:3000/post/"User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
        #name=("User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
        #cv2.imshow('image',img)
        #print(img)

        #img_im =cv2.cvtColor(gray[y:y+h,x:x+w], cv2.COLOR_BGR2RGB)
        #image = np.array(img_im)
        #image = image.tostring()
        #print(image)
        image = gray[y:y+h,x:x+w]


                
        #img_im=np.array(img_im)
        #img_im = np.abs(np.fft.fftshift(numpy.fft.fft2(img_im)))
        #pil_im = Image.fromarray(img_im)
        #pil_im.save('mypic.png')
        #print(pil_im)
        #img_numpy = np.array(pil_im,'uint8')
        #stream = StringIO()
        #stream = BytesIO()
        #pil_im.save(stream, format="JPEG")
        #print(pil_im)
        #stream.seek(0)
        #pil_im.save(name)
        #img_for_post = img_numpy
        #img_for_post = stream.read()
        
       # with open(img_for_post,"rb") as imageFile:
        #    img_for_post = base64.b64encode(imageFile.read())
        #img_for_post = np.array(img_for_post)
        files = {'image.'+str(face_id)+'.'+str(count):(image,'rb')}
        #print(files)
        response = requests.post(
            url = "http://localhost:3000/ImageData/",
            data = files )
    k=cv2.waitKey(100) & 0xff
    if k==27:
        break
    elif count >=30:
        break
print("\n [INFO] Exciting Program and Cleanup stuff")
cam.release()
cv2.destroyAllWindows()
