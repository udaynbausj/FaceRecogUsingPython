import cv2
import numpy as np

facedetect = cv2.CascadeClassifier("D:\\UDAY\\SOFTWARES\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)
ID = print("Enter the User ID : ")
sampleNum = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataset/user"+str(ID)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+h])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)==ord('q')
    if(sampleNum>20):
        break
cv2.release()
cv2.destroyAllWindows()