import datetime
import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2

class VideoProcessingController:

    def DetectedObjects(self,path):
            vid = cv2.VideoCapture(path)
            fps = vid.get(cv2.CAP_PROP_FPS)
            frames = vid.get(cv2.CAP_PROP_FRAME_COUNT)

            #videoDuration=int(frames/fps)
            finalOutput=[]
            c=1
            model=torch.hub.load('ultralytics/yolov5', 'yolov5s')
            
            while vid.isOpened():
                   ret, frame = vid.read()
                   t=c/fps
                   a='{}'.format(datetime.timedelta(seconds=t))
                   # Make detections 
                   results = model(frame)
                   x=results.pandas().xyxy[0]
                   for i in range(x.shape[0]):
                           b={}
                           b['FrameNumber']=c
                           b['Name']=x.loc[i,'name']
                           b['TimeStamp']=a
                           b['Accuracy']=x.loc[i,'confidence']
                           finalOutput.append(b)
                   c+=1
        
        
                   if c==frames-1:
                        break
                   

            return finalOutput