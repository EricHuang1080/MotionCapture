#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import time

def RGB_location():
    # Step 1: Read the image

    image = cv2.imread("1108RGB.jpeg")                  #this line is just for test run
#    if image is None:
#        print("Error: Could not load the image.")
#        return

#    cap = cv2.VideoCapture(0)  # Open the default camera
#    time.sleep(0.1)
#    if not cap.isOpened():
#        print("Error: Could not open the camera.")
#        return None

    # Capture one frame
    
#    ret, image = cap.read()
#    cap.release()  # Release the camera

    # Step 2: Convert to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Step 3: Define color ranges in HSV for red, green, and blue
    

    # Light Red color range
    lower_red1 = np.array([0, 50, 200])   # Light red has higher V (brightness)
    upper_red1 = np.array([10, 150, 255])
    lower_red2 = np.array([170, 50, 200])
    upper_red2 = np.array([180, 150, 255])
    
    lower_pink = np.array([140, 50, 150])  # Lighter pink tones (high brightness and saturation)
    upper_pink = np.array([170, 255, 255])
    
    # Light Green color range
    lower_green = np.array([36, 50, 200])  # Light green with higher V
    upper_green = np.array([89, 150, 255])
    
    # Light Orange color range
    lower_orange = np.array([10, 100, 200])   # Adjust for lighter, brighter orange
    upper_orange = np.array([25, 255, 255])

    # Step 4: Create masks for each color
    # Red mask
    #mask_red1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    #mask_red2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    #red_mask = cv2.bitwise_or(mask_red1, mask_red2)

    pink_mask = cv2.inRange(hsv_image, lower_pink, upper_pink)

    # Green mask
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Blue mask
    blue_mask = cv2.inRange(hsv_image, lower_orange, upper_orange)

    # Step 5: Find mean positions of each color

    # Find red pixel positions and calculate mean
    red_pixel_positions = np.column_stack(np.where(pink_mask > 0))
    if len(red_pixel_positions) > 0:
        R = red_pixel_positions.mean(axis=0)
        R = (int(R[1]), int(R[0]))  # Mean position as (x, y)
#        print(f"Mean position of red pixels (R): {R}")
    else:
        R = None
        print("No red pixels found.")

    # Find green pixel positions and calculate mean
    green_pixel_positions = np.column_stack(np.where(green_mask > 0))
    if len(green_pixel_positions) > 0:
        G = green_pixel_positions.mean(axis=0)
        G = (int(G[1]), int(G[0]))  # Mean position as (x, y)
#        print(f"Mean position of green pixels (G): {G}")
    else:
        G = None
        print("No green pixels found.")

    # Find blue pixel positions and calculate mean
    blue_pixel_positions = np.column_stack(np.where(blue_mask > 0))
    if len(blue_pixel_positions) > 0:
        B = blue_pixel_positions.mean(axis=0)
        B = (int(B[1]), int(B[0]))  # Mean position as (x, y)
#        print(f"Mean position of blue pixels (B): {B}")
    else:
        B = None
        print("No blue pixels found.")

    # Step 6: Add text labels at the mean positions
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    if R:
        cv2.putText(image, 'R', R, font, font_scale, (0, 0, 255), thickness, cv2.LINE_AA)  # Red text for red mean
    if G:
        cv2.putText(image, 'G', G, font, font_scale, (0, 255, 0), thickness, cv2.LINE_AA)  # Green text for green mean
    if B:
        #temporally use orange for blue
        cv2.putText(image, 'O', B, font, font_scale, (255, 0, 0), thickness, cv2.LINE_AA)  # Blue text for blue mean
 #       cv2.putText(image, 'B', B, font, font_scale, (255, 0, 0), thickness, cv2.LINE_AA)  # Blue text for blue mean

    # Display the image with the mean positions labeled
    cv2.imshow("Mean Color Positions", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    y_center,x_center = image.shape[:2]
#    print(x_center,y_center)
    x_center=x_center/2.
    y_center=y_center/2.
    R=[R[0]-x_center,R[1]-y_center]
    G=[G[0]-x_center,G[1]-y_center]
    B=[B[0]-x_center,B[1]-y_center]
#    in this example, B is the origin, R is on +x, G is on +y, and S is the camera
#    return ([R,G,B])
    #return (origin, +x, +y)
    return ([R,B,G])


aaa=RGB_location()


# In[ ]:




