from os import name
import face_recognition
from PIL import Image, ImageDraw
import cv2
import base64
import os
class FaceDetector:
    
    def detect_faces(self,image_file):
        outline_color = 'blue'
        image = face_recognition.load_image_file(image_file)
        face_locations = face_recognition.face_locations(image)
        number_of_faces = len(face_locations)
        a="I found {} face(s) in this photograph.".format(number_of_faces)
        for face_loc in face_locations:
                y1,x1,y2,x2=face_loc
                h=y2-y1
                w=x1-x2
                im=cv2.rectangle(image,(x2,y1),(x2+w,y1+h),(0,255,0),2)
        im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        name='im.jpg'
        path=r'.\storage\uploads\\'+name
        cv2.imwrite(path,im)
        with open(path,'rb') as f:
             data=base64.b64encode(f.read())
        os.remove(path)
        
        return {"image_data":str(data),'details':a}