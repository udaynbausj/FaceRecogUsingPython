import cv2
from shutil import *
import os
import time
import re
from .main import user

file = open("testfile.txt","w")
file.write("NAME")
file.write(",")
file.write("REGD.NO")
file.write(",")
file.write("DATE,TIME")
file.write("\n")
user = '0'
folder = '0'


def recognise():
    facecascade = cv2.CascadeClassifier('D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml')
    eyecascade = cv2.CascadeClassifier('D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\\data\\haarcascades\\haarcascade_eye.xml')
    rec = cv2.face.createLBPHFaceRecognizer()
    rec.load('C:\\Users\\MY PC\\PycharmProjects\\untitled\\recogniser\\recogniser_all.yml')
    user = '0'
    camera = cv2.VideoCapture(0)
    sampleNum = 0
    folder = '0'
    font = cv2.FONT_HERSHEY_DUPLEX
    while(True):
        ret,frame = camera.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = facecascade.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            sampleNum = sampleNum + 1
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            folder,conf = rec.predict(gray[y:y+h,x:x+w])
            cv2.putText(frame,str(folder),(x,y+h),font,2,255)
            f = cv2.resize(gray[y:y+h,x:x+h],(500,500))
            cv2.waitKey(100)
        cv2.imshow("camera : ",frame)
        cv2.waitKey(1)
        if sampleNum>15:
            break
    camera.release()
    cv2.destroyAllWindows()

recognise()

def recognise1():
    facecascade = cv2.CascadeClassifier('D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml')
    eyecascade = cv2.CascadeClassifier('D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\\data\\haarcascades\\haarcascade_eye.xml')
    rec = cv2.face.createLBPHFaceRecognizer()
    rec.load('C:\\Users\\MY PC\\PycharmProjects\\untitled\\recogniser\\recogniser_all.yml')
    user = '0'
    camera = cv2.VideoCapture(0)
    sampleNum = 0
    folder = '0'
    font = cv2.FONT_HERSHEY_DUPLEX
    while(True):
        ret,frame = camera.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = facecascade.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            sampleNum = sampleNum + 1
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            folder,conf = rec.predict(gray[y:y+h,x:x+w])
            cv2.putText(frame,str(folder),(x,y+h),font,2,255)
            f = cv2.resize(gray[y:y+h,x:x+h],(500,500))
            file.write(user)
            file.write(",")
            file.write(str(folder))
            file.write(",")
            file.write(time.strftime("%d/%m/%y"))
            file.write(",")
            file.write(time.strftime("%I:%M:%S"))
            file.write("\n")
            cv2.waitKey(10)
        cv2.imshow("camera : ",frame)
        cv2.waitKey(1)
        if sampleNum>1:
            break
    camera.release()
    cv2.destroyAllWindows()

recognise1()