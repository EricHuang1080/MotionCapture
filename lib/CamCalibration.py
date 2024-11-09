#!/usr/bin/env python
# coding: utf-8
import cv2
import numpy as np
from .CreateCAM import add_camera_name,set_camera_pixelVector

def map_range(values, source_min, source_max, target_min, target_max):
    # Convert input values to a NumPy array
    values = np.array(values)
    
    # Apply the mapping formula
    mapped_values = target_min + (values - source_min) * (target_max - target_min) / (source_max - source_min)
    return mapped_values



def camera_calibration(CamName,realZ,realX,realY,filename):
   # CamName=input("Please enter camera name")
    add_camera_name(CamName)
    
    # Read the image
    #pic=input("Please enter the picture taken by this camera")
    #realZ=float(input("Please enter the height from where you took (cm): "))
    image = cv2.imread(filename)
    
    # Check if the image was successfully loaded
    if image is None:
        print("Error: Could not load image.")
    #else:
        # Display the image
        #cv2.imshow("Loaded Image", image)
        #cv2.waitKey(0)  # Wait for a key press to close the window
        #cv2.destroyAllWindows()
    
    
    pixelX, pixelY = image.shape[:2]
    
    print("Picture size",pixelX, pixelY)
  #  realX=float(input("Please Pic X in cm: "))
  #  realY=float(input("Please Pic Y in cm: "))
    realX=realX/realZ 
    realY=realY/realZ
    #map pixel on to real
    source_range_x = (0, pixelX) 
    target_range_x = (0, realX)  
    
    source_range_y = (0, pixelY) 
    target_range_y = (0, realY)   
    
    values_to_map = [0,1]
    
    # Map the values using the function
    mapped_values_x = map_range(values_to_map, source_range_x[0], source_range_x[1], target_range_x[0], target_range_x[1])
    mapped_values_y = map_range(values_to_map, source_range_y[0], source_range_y[1], target_range_y[0], target_range_y[1])
    
    print("Mapped Values:", mapped_values_x)
    print("Mapped Values:", mapped_values_y)
    
    
    set_camera_pixelVector(CamName,[mapped_values_x[1],mapped_values_y[1],1],'CamID.json')
