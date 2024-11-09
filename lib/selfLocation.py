#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sympy import symbols, Eq, solve
from sympy import real_root
import json
from scipy.optimize import fsolve
from .CreateCAM import set_camera_location,set_camera_orientation
from .PicLocating import RGB_location
   

# Define initial variables
#with open('CamID.json', 'r') as file:
#    cameras = json.load(file)
#for camera in cameras:
##    if (camera.get("name")) == 'EricsPad':
#        pV=camera.get('pixelVector')
        
#these should later be inputs

tt1=0.0
tt2=0.0
tt3=0.0

def t_to_tCheck(t1,camName,a_pixel,b_pixel,c_pixel,AB_square ,AC_square,BC_square ,filename='CamID.json'):
    #let A be origin, B on +x, C on +y
    """
    Calculate and check the transformation parameters t2, t3, and t1_check for a given camera setup.

    This function uses the provided pixel vectors for points A, B, and C along with the camera's pixel 
    vector to calculate the scale factors t2 and t3, and checks t1 using symbolic computation. It 
    evaluates equations based on the distances AB, BC, and AC and finds the corresponding transformation 
    parameters that minimize the error with respect to the given t1.

    Parameters:
    - t1 (float): Initial transformation parameter for point A.
    - camName (str): The name of the camera to retrieve pixel vector data from.
    - a_pixel (np.array): Pixel vector for point A.
    - b_pixel (np.array): Pixel vector for point B.
    - c_pixel (np.array): Pixel vector for point C.
    - AB_square (float): The squared distance constraint between points A and B.
    - AC_square (float): The squared distance constraint between points A and C.
    - BC_square (float): The squared distance constraint between points B and C.
    - filename (str): The JSON file name where camera data is stored. Defaults to 'CamID.json'.

    Returns:
    - float: The error of the best found t1_check compared to the input t1.
    """
    with open(filename, 'r') as file:
        cameras = json.load(file)
    for camera in cameras:
        if (camera.get("name")) == camName:
            pixelVector=np.array(camera.get('pixelVector'))
            break
#    print(type(a_pixel))    
#    print(type(pixelVector))        
    a=a_pixel*pixelVector
    b=b_pixel*pixelVector
    c=c_pixel*pixelVector
    
    t1s=np.array([], dtype=float)
    t2s=np.array([], dtype=float)
    t3s=np.array([], dtype=float)
    
    
    # Define symbolic variables for t2, t3, and t1_check
    t1_check, t2, t3 = symbols('t1_check t2 t3', real=True)

    A = a * t1
    eqAB = Eq(np.sum((b * t2 - A) ** 2), AB_square)
    # Solve for t2 based on eqAB
    T2_values = solve(eqAB, t2)
#    print(T2_values)
    for T2 in T2_values:
        if T2.is_real:
            t2s=np.append(t2s,T2)
            B = b * float(T2)
            eqBC = Eq(np.sum((c * t3 - B) ** 2), BC_square)

            # Solve for t3 based on eqBC
            T3_values = solve(eqBC, t3)
 #           print(T3_values)
            for T3 in T3_values:
                
                if T3.is_real:
                    t3s=np.append(t3s,T2)
                    C = c * float(T3)
                    eqAC = Eq(np.sum((C - a * t1_check) ** 2), AC_square)

                    # Solve for t1_check based on eqAC
                    T1_values = solve(eqAC, t1_check)
                    for T1 in T1_values:
                        t1s=np.append(t1s,T1)
    index=np.argmin(abs(t1s-t1))    
    error=float(t1s[index])
    error=(error-t1)/t1   
    print("Error=",100*error,"%")     
    global tt1,tt2,tt3
    tt1= t1s[index]
    tt2= t2s[index//4]
    tt3= t3s[index//2]
                                      
    return(float(t1s[index])-t1)     


    t1s=np.array([1,4,2,5,6])
    error=float(t1s[index])


# In[13]:


def solve_with_fallback(initial_guess,camName,R_pixel,B_pixel,G_pixel,AB_square,AC_square,BC_square,filename='CamID.json'):
    
    """
    Solve for the position of a camera based on the RGB values of a checkerboard and the square of the distances between the corners of the checkerboard.
    
    Parameters
    ----------
    initial_guess : float
        Initial guess for tt1
    camName : str
        Name of the camera
    R_pixel, B_pixel, G_pixel : floats
        RGB values of the checkerboard
    AB_square, AC_square, BC_square : floats
        Squares of the distances between the corners of the checkerboard
    filename : str, optional
        Name of the json file with the camera information. Default is 'CamID.json'
    
    Returns
    -------
    R, B, G : 3-element arrays
        Position of the camera in the RGB coordinate system
    """
    global tt1,tt2,tt3
    with open(filename, 'r') as file:
        cameras = json.load(file)
    for camera in cameras:
        if (camera.get("name")) == camName:
            pixelVector=np.array(camera.get('pixelVector'))
            break
    try:
        # Use fsolve to find the root
        
        root, info, ier, msg = fsolve(t_to_tCheck, initial_guess, full_output=True,args=("1108webcam",R_pixel,B_pixel,G_pixel,AB_square,AC_square,BC_square,'CamID.json'))
        
        # Check if fsolve succeeded (ier == 1 means success)
        if ier != 1:
            print("fsolve failed to converge", root)
        
        # Verify if the solution meets our expectations (e.g., within tolerance)
        
        if not np.isclose(t_to_tCheck(root,"1108webcam",R_pixel,B_pixel,G_pixel,AB_square,AC_square,BC_square,'CamID.json'), 0, atol=1e-5):
            print("Solution did not meet tolerance", root)
        
        print(f"Root found: {root[0]}")

        R=R_pixel*pixelVector*tt1
        B=B_pixel*pixelVector*tt2
        G=G_pixel*pixelVector*tt3
        tt1=0
        tt2=0
        tt3=0
        return  [R,B,G]

    except ValueError as e:
        print(f"optimization unable to proceed ")
       # global tt1,tt2,tt3
        R=R_pixel*pixelVector*tt1
        B=B_pixel*pixelVector*tt2
        G=G_pixel*pixelVector*tt3
        tt1=0
        tt2=0
        tt3=0
        return  [R,B,G]


# In[34]:


#let B be origin, A on +x, C on +y,S be camera
def find_camera_placing(camName,x_square ,y_square ,xy_square,initial_guess=400,filename='CamID.json'):
    """
    Set camera placing in the camera coordinate system.
    
    This function takes a camera name, x and y coordinates of the unit square, and the initial guess for the optimization,
    and returns the location of the camera origin, and the unit vectors of the x and y axes in the camera coordinate system.
    
    Parameters:
    - camName (str): The name of the camera to place.
    - x_square (float): The x coordinate of the unit square.
    - y_square (float): The y coordinate of the unit square.
    - xy_square (float): The x,y coordinate of the unit square.
    - initial_guess (float): The initial guess for the optimization. Defaults to 400.
    - filename (str): The JSON file name where camera data is stored. Defaults to 'CamID.json'.
    
    Returns:
    - OS (np.array): The location of the camera origin.
    - unitX (np.array): The unit vector of the x axis in the camera coordinate system.
    - unitY (np.array): The unit vector of the y axis in the camera coordinate system.
    - unitZ (np.array): The unit vector of the z axis in the camera coordinate system.
    """
    RGB=RGB_location()
#   print(RGB)
    origin_pixel=[RGB[0][0],RGB[0][1],1.]
    x_pixel=[RGB[1][0],RGB[1][1],1]
    y_pixel=[RGB[2][0],RGB[2][1],1]
#    print(type(origin_pixel[0]))
#    print(type(x_pixel[0]))
    OXY=solve_with_fallback(initial_guess,camName,x_pixel,origin_pixel,y_pixel,x_square,y_square,xy_square,'CamID.json')
    OS=OXY[0][:]
    OX=np.array(OXY[1][:]-OXY[0][:], dtype=np.float64)
    OY=np.array(OXY[2][:]-OXY[0][:], dtype=np.float64)
    
    unitX=OX/np.sqrt(np.sum((OX)**2))
    unitY=OY/np.sqrt(np.sum((OY)**2))
    unitZ=np.cross(unitX,unitY)
    
    return(OS,unitX,unitY,unitZ)
    
  
    

    
    



# In[36]:
def marching_guessing(camName,x_square ,y_square ,xy_square):
    """
    This function marches through initial guesses to find a solution for the location of camera and its orientation.
    
    Parameters:
    camName (str): The name of the camera
    x_square (float): The square of the distance of the x pixel from the origin
    y_square (float): The square of the distance of the y pixel from the origin
    xy_square (float): The square of the distance of the x pixel from the y pixel
    
    Returns:
    None
    
    Notes:
    This function will keep increasing the initial guess until it finds a solution.
    If it is unable to find a solution, it will print a message and continue to the next iteration.
    """
    for i in range(20,100):#range(1,100):
        i=i*3
        OS,unitX,unitY,unitZ=find_camera_placing(camName,x_square ,y_square ,xy_square,i,filename='CamID.json')

        CamLoca=[float(np.dot(OS,unitX)),
                float(np.dot(OS,unitY)),
                float(np.dot(OS,unitZ))]
        print("initial guess:",i,"     location:",CamLoca)
        print("orthogonality check : ",np.dot(unitX,unitY))
        if (abs(np.dot(unitX,unitY))<=0.001):
            print(sum(unitX**2))
            print(sum(unitY**2))
            print(sum(unitZ**2))
            CamLoca=[float(np.dot(OS,unitX)),
                    float(np.dot(OS,unitY)),
                    float(np.dot(OS,unitZ))]
            print("location:",CamLoca)
            #dot product of (1,0,0) and unitX,unitY unitZ respectively
            CamOrien_X=[float(unitX[0]),
                    float(unitY[0]),
                    float(unitZ[0])]
            CamOrien_Y=[float(unitX[1]),
                    float(unitY[1]),
                    float(unitZ[1])]
            #in right hand system, z is on 
            CamOrien_Z=[-float(unitX[2]),
                    -float(unitY[2]),
                    -float(unitZ[2])]
            set_camera_location(camName,CamLoca,'CamID.json')
            set_camera_orientation(camName,CamOrien_X,CamOrien_Y,CamOrien_Z,'CamID.json')
            return (CamLoca,CamOrien_X,CamOrien_Y,CamOrien_Z)
        else:
            print("unable to find solution")
            continue
            
            

        
marching_guessing("1108webcam",400,900,1300)