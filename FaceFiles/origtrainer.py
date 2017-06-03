import cv2
import os
import numpy as np
from PIL import Image
from main import folder1,user1

recogniser = cv2.face.createLBPHFaceRecognizer()
path = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\15BCE0656'

def getimageIds(path):
    imagepaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagepath in imagepaths:
        faceimg = Image.open(imagepath).convert('L')
        facenp = np.array(faceimg,'uint8')
        Id = int(os.path.split(imagepath)[-1].split('.')[1])
        faces.append(facenp)
        Ids.append(Id)
        cv2.imshow('Training the dataset',facenp)
        cv2.waitKey(10)
    return np.array(Ids),faces
Ids,faces = getimageIds(path)
recogniser.train(faces,np.array(Ids))
recogniser.save('recogniser/'+folder1+'.yml')
cv2.destroyAllWindows()