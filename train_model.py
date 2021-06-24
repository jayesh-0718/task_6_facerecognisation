import cv2
import numpy as np
import os
import joblib
from os import listdir
from os.path  import isfile, join
# Get training data we previously made
data_path = './face/user/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    # Create arrays from training data and labels
Training_Data, Labels = [], []

    # Open training images in our datapath
    # Create a numpy array for training data
for i, files in enumerate(onlyfiles):

    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    ID=int(os.path.split(image_path)[-1].split(".")[1]) #getting the Id from the image

    Labels.append(ID)
    
    # Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)

    # Initialize facial recognizer
    # model = cv2.face.createLBPHFaceRecognizer()
    # NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()
    # pip install opencv-contrib-python
    # model = cv2.createLBPHFaceRecognizer()
    
abhi_model = cv2.face_LBPHFaceRecognizer.create()
    # Let's train our model 
abhi_model.train(np.asarray(Training_Data), np.asarray(Labels))
    # Save the model


print("Model trained  And Saved Sucessefully....")
