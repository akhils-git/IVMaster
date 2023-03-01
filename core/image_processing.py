# import cv2
import numpy as np
import pandas as pd
import torch
from torchvision import transforms
from PIL import Image

# Define the object detection class


class ImageProcessingController:

    def object_detection(self, image_path):

        # Load input image
        # img = Image.open(image_path)
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        # Run object detection
        results = model(image_path)

        # Extract object details
        x = results.pandas().xyxy[0]
        objects = []
        for i in range(x.shape[0]-1):
            obj = {
                'Name': x.loc[i, 'name'],
                'Accuracy': x.loc[i, 'confidence'],
                'UpperRightX': x.loc[i, 'xmin'],
                'UpperRightY': x.loc[i, 'ymin'],
                'BottomLeftX': x.loc[i, 'xmax'],
                'BottomLeftY': x.loc[i, 'ymax']
            }
            objects.append(obj)

        return objects
