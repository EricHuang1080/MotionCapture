#!/usr/bin/env python
# coding: utf-8
import numpy as np
import json
from .PicLocating import RGB_location
from .coord_transform import position_to_world_coordinate,rotate_vector_to_world_coordinate

def direction_vector_from_camera(CamName,image):
    #read orientation and pixelVector from json
    with open('CamID.json', 'r') as file:
        cameras = json.load(file)
    for camera in cameras:
        if (camera.get("name")) == CamName:
            pV=camera.get('pixelVector')
            CamLoca=camera.get('location')
            CamOrien_X=camera.get('orientation_X')
            CamOrien_Y=camera.get('orientation_Y')
            CamOrien_Z=camera.get('orientation_Z')
            print(CamLoca)
    
    #find point by PicLocating and find real world direction vector
    RGB=RGB_location(image)
    print(type(RGB[0][0]))
    print(type(pV[0]))
          
    pV[0]=RGB[0][0]*pV[0]
    pV[1]=RGB[0][1]*pV[1]
    print(pV)
    
    #convert to world coordinate
    direction_vector=rotate_vector_to_world_coordinate(pV, CamOrien_X, CamOrien_Y, CamOrien_Z)

    A=(np.eye(3)-direction_vector@(direction_vector.T))
    P=A@CamLoca
    print(A)
    print(P)
                                                       
    return direction_vector,A,P

#try capturing red point
RGB=RGB_location('RGBcalibration.jpeg')[0]

#For multiple cameras, just sum A and P 
V,A,P=direction_vector_from_camera("EricsPad",'RGBcalibration.jpeg')

#least square method
antiA=np.linalg.inv(A)
position=antiA@P




