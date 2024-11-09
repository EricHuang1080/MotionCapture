#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Function to add a camera's name
import json
import os

def add_camera_name(name, filename='CamID.json'):

    message = None
    
    # Check if the file exists
    if not os.path.exists(filename):
        # If file does not exist, create it with an empty list
        with open(filename, 'w') as file:
            json.dump([], file)  # Initialize with an empty list

    try:
        # Read existing cameras from the JSON file
        with open(filename, 'r') as file:
            cameras = json.load(file)

            # Ensure that the data loaded is a list
            if not isinstance(cameras, list):
                raise ValueError("The JSON file must contain a list of cameras.")
                
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        # Handle case where the JSON file is corrupted or empty
        print(f"Warning: {e}. Initializing with an empty list.")
        
        cameras = []

    # Check if the camera already exists to avoid duplicates
    if any(camera.get("name") == name for camera in cameras):
        print(f"Camera '{name}' already exists.")
        return

    # Append the new camera data
    camera_data = {"name": name}
    cameras.append(camera_data)

    # Write the updated camera list back to the JSON file
    with open(filename, 'w') as file:
        json.dump(cameras, file, indent=4)

    print(f"Camera '{name}' added successfully!")
# Function to add a camera's pixelVector
def set_camera_pixelVector(name, pixelVector, filename='CamID.json'):
    
    
    try:
        # Read existing cameras from the JSON file
        with open(filename, 'r') as file:
            cameras = json.load(file)
    except FileNotFoundError:
        print("No camera found. Please add a camera name first.")
        return

    # Find the camera by name
    for camera in cameras:
        if camera["name"] == name:
            camera["pixelVector"] = pixelVector
            break
    else:
        print(f"Camera '{name}' not found. Please add the name first.")
        return

    # Write the updated camera list back to the JSON file
    with open(filename, 'w') as file:
        json.dump(cameras, file, indent=4)

    print(f"pixelVector for '{name}' updated successfully!")

def set_camera_location(name, location, filename='CamID.json'):
    
    
    try:
        # Read existing cameras from the JSON file
        with open(filename, 'r') as file:
            cameras = json.load(file)
    except FileNotFoundError:
        print("No camera found. Please add a camera name first.")
        return

    # Find the camera by name
    for camera in cameras:
        if camera["name"] == name:
            camera["location"] = location
            break
    else:
        print(f"Camera '{name}' not found. Please add the name first.")
        return

    # Write the updated camera list back to the JSON file
    with open(filename, 'w') as file:
        json.dump(cameras, file, indent=4)

    print(f"location for '{name}' updated successfully!")

def set_camera_orientation(name, orientation_x, orientation_y, orientation_z, filename='CamID.json'):
    try:
        # Read existing cameras from the JSON file
        with open(filename, 'r') as file:
            cameras = json.load(file)
    except FileNotFoundError:
        print("No camera found. Please add a camera name first.")
        return

    # Find the camera by name
    for camera in cameras:
        if camera["name"] == name:
            camera["orientation_X"] = orientation_x
            camera["orientation_Y"] = orientation_y
            camera["orientation_Z"] = orientation_z
            break
    else:
        print(f"Camera '{name}' not found. Please add the name first.")
        return

    # Write the updated camera list back to the JSON file
    with open(filename, 'w') as file:
        json.dump(cameras, file, indent=4)

    print(f"orientation for '{name}' updated successfully!")

# Function to display cameras
def display_cameras(filename='CamID.json'):
    try:
        with open(filename, 'r') as file:
            cameras = json.load(file)
            for camera in cameras:
                print(camera)
    except FileNotFoundError:
        print("No cameras found.")


# In[ ]:





# In[ ]:




