'''import cgitb cgitb.enable()
start_response('200 OK',[('Content-Type','text/html')])'''

from __future__ import division
import time
import cv2
import os


# Import the PCA9685 module.
import Adafruit_PCA9685
# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
cam = cv2.VideoCapture(-1)
cam .set(3,640)
cam.set(4,480)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('\n enter user id end press <return> ==> ')
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
        #cv2.imwrite("dataset/User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
        #cv2.imwrite("file://192.168.42.230/ImageData/User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w]) 

        cv2.imshow('image',img)
        if count>0:
             pwm.set_pwm(3, 0, servo_min)
             time.sleep(1)
             pwm.set_pwm(3, 0, servo_max)
             time.sleep(1)
             pwm.set_pwm(2, 0, servo_min)
             time.sleep(1)
             pwm.set_pwm(2, 0, servo_max)
             time.sleep(1)
    k=cv2.waitKey(100) & 0xff
    if k==27:
        count = 0
        break
    elif count >=30:
        break
print("\n [INFO] Exciting Program and Cleanup stuff")
cam.release()
cv2.destroyAllWindows()


