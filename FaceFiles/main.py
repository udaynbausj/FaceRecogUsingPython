import cv2
from shutil import *
import os
sampleNum = 0
folder = input("\nEnter your Registration number's numerical part : ")
user = input("\nEnter Your name : ")

user1 = user

copy2('C:\\Users\\MY PC\\PycharmProjects\\untitled\\try1.py','C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images')
sampleNum = 0
facecascade = cv2.CascadeClassifier('D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml')
eyecascade = cv2.CascadeClassifier('D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\\data\\haarcascades\\haarcascade_eye.xml')
camera = cv2.VideoCapture(0)
count = 0
while(True):
    ret,frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum = sampleNum + 1
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        f = cv2.resize(gray[y:y+h,x:x+h],(500,500))
        cv2.imwrite("Images/"+user+"."+str(folder)+"."+str(sampleNum)+".jpg",f )
        count+=1
        cv2.waitKey(200)
    cv2.imshow("camera : ",frame)
    cv2.waitKey(1)
    if sampleNum>25:
        break
os.remove('C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images\\try1.py')
camera.release()
cv2.destroyAllWindows()