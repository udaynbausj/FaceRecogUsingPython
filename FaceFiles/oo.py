from shutil import *
class detect:
    folder = input("\nEnter your Registration number's numerical part : ")
    user = input("\nEnter Your name : ")
    def __init__(self):
        import cv2
        import os
        sampleNum = 0
        folder = input("\nEnter your Registration number's numerical part : ")
        user = input("\nEnter Your name : ")


        copy2('C:\\Users\\MY PC\\PycharmProjects\\untitled\\try1.py',
              'C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images')
        sampleNum = 0
        facecascade = cv2.CascadeClassifier(
            'D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml')
        eyecascade = cv2.CascadeClassifier(
            'D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\\data\\haarcascades\\haarcascade_eye.xml')
        camera = cv2.VideoCapture(0)
        count = 0
        while (True):
            ret, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = facecascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                sampleNum = sampleNum + 1
                img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                f = cv2.resize(gray[y:y + h, x:x + h], (500, 500))
                cv2.imwrite("Images/" + user + "." + str(folder) + "." + str(sampleNum) + ".jpg", f)
                count += 1
                cv2.waitKey(200)
            cv2.imshow("camera : ", frame)
            cv2.waitKey(1)
            if sampleNum > 25:
                break
        os.remove('C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images\\try1.py')
        camera.release()
        cv2.destroyAllWindows()
class trainer:
    def __init__(self):
        import cv2
        import os
        import numpy as np
        from PIL import Image

        recogniser = cv2.face.createLBPHFaceRecognizer()
        path = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images'

        def getimageIds(path):
            imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
            faces = []
            Ids = []
            for imagepath in imagepaths:
                faceimg = Image.open(imagepath).convert('L')
                facenp = np.array(faceimg, 'uint8')
                Id = int(os.path.split(imagepath)[-1].split('.')[1])
                faces.append(facenp)
                print(Id)
                Ids.append(Id)
                cv2.imshow('Training the dataset', facenp)
                cv2.waitKey(10)
            return Ids, faces

        Ids, faces = getimageIds(path)
        recogniser.train(faces, np.array(Ids))
        recogniser.save('recogniser/recogniser_all.yml')
        cv2.destroyAllWindows()

class recog(detect,trainer):
    import os
    path = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images'
    imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
    path = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images'
    for imagepath in imagepaths:
        ID = int(os.path.split(imagepath)[-1].split('.')[1])
    imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
    path = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images'
    def __init__(self):
        import cv2
        import os
        import time
        import re
        file = open("testfile.txt", "w")
        file.write("NAME")
        file.write(",")
        file.write("REGD.NO")
        file.write(",")
        file.write("DATE,TIME")
        file.write("\n")
        folder = '0'

        def recognise():
            path = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images'
            imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
            path = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images'
            for imagepath in imagepaths:
                ID = int(os.path.split(imagepath)[-1].split('.')[1])
            facecascade = cv2.CascadeClassifier(
                'D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml')
            eyecascade = cv2.CascadeClassifier(
                'D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\\data\\haarcascades\\haarcascade_eye.xml')
            rec = cv2.face.createLBPHFaceRecognizer()
            rec.load('C:\\Users\\MY PC\\PycharmProjects\\untitled\\recogniser\\recogniser_all.yml')
            camera = cv2.VideoCapture(0)
            sampleNum = 0
            folder = '0'
            font = cv2.FONT_HERSHEY_DUPLEX
            while (True):
                ret, frame = camera.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = facecascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    sampleNum = sampleNum + 1
                    img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    folder, conf = rec.predict(gray[y:y + h, x:x + w])
                    cv2.putText(frame, str(folder), (x, y + h), font, 2, 255)
                    f = cv2.resize(gray[y:y + h, x:x + h], (500, 500))
                    cv2.waitKey(100)
                cv2.imshow("camera : ", frame)
                cv2.waitKey(1)
                if sampleNum > 15:
                    break
            camera.release()
            cv2.destroyAllWindows()

        recognise()

        def recognise1():
            path = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images'
            imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
            path = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\Images'
            for imagepath in imagepaths:
                ID = int(os.path.split(imagepath)[-1].split('.')[1])
            facecascade = cv2.CascadeClassifier(
                'D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml')
            eyecascade = cv2.CascadeClassifier(
                'D:\\UDAY\\SOFTWARES\\opencv\\sources\\OpenCV Master\\opencv-master\\data\\haarcascades\\haarcascade_eye.xml')
            rec = cv2.face.createLBPHFaceRecognizer()
            rec.load('C:\\Users\\MY PC\\PycharmProjects\\untitled\\recogniser\\recogniser_all.yml')
            camera = cv2.VideoCapture(0)
            sampleNum = 0
            folder = '0'
            font = cv2.FONT_HERSHEY_DUPLEX
            while (True):
                ret, frame = camera.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = facecascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    sampleNum = sampleNum + 1
                    img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    folder, conf = rec.predict(gray[y:y + h, x:x + w])
                    cv2.putText(frame, str(folder), (x, y + h), font, 2, 255)
                    f = cv2.resize(gray[y:y + h, x:x + h], (500, 500))
                    file.write(str(os.path.split(imagepath)[-1].split('.')[0]))
                    file.write(",")
                    file.write(str(os.path.split(imagepath)[-1].split('.')[1]))
                    file.write(",")
                    file.write(time.strftime("%d/%m/%y"))
                    file.write(",")
                    file.write(time.strftime("%I:%M:%S"))
                    file.write("\n")
                    cv2.waitKey(10)
                cv2.imshow("camera : ", frame)
                cv2.waitKey(1)
                if sampleNum > 0:
                    break
            camera.release()
            cv2.destroyAllWindows()

        recognise1()
detect1 = detect()
trainer1 = trainer()
#recog2 = recog()

