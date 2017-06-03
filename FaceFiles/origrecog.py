import cv2
from shutil import *
import os



facecascade = cv2.CascadeClassifier('D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml')
eyecascade = cv2.CascadeClassifier('D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\\data\\haarcascades\\haarcascade_eye.xml')
rec = cv2.face.createLBPHFaceRecognizer()
rec.load('C:\\Users\\MY PC\\PycharmProjects\\untitled\\recogniser\\'+folder+'\\.yml')
camera = cv2.VideoCapture(0)
sampleNum = 0
id = 0
font = cv2.FONT_HERSHEY_COMPLEX_SMALL,5,1,0,1
while(True):
    ret,frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum = sampleNum + 1
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        cv2.putText(str(user),(x,y+h),font,255)
        f = cv2.resize(gray[y:y+h,x:x+h],(500,500))
        cv2.waitKey(100)
    cv2.imshow("camera : ",frame)
    cv2.waitKey(1)
    if sampleNum>25:
        break
os.remove('C:\\Users\\MY PC\\PycharmProjects\\untitled\\'+folder+'\\try2.py')
camera.release()
cv2.destroyAllWindows()