from lib import CamCalibration as CC
import cv2
import time


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)  # Open the default camera
    time.sleep(1)
    while cap.isOpened():
        ret, frame = cap.read()

        cv2.imshow("Webcam", frame)
    # 按 'q' 鍵退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
#    cv2.imwrite("1108RGB.jpeg", frame)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#    cv2.waitKey(1)
    CamID=input("Please enter camera name")
    real_x=float(input("Please enter real x"))
    real_y=float(input("Please enter real y"))
    height=float(input("please enter height"))
     
    CC.camera_calibration(CamID,height,real_x,real_y,"1108.jpeg")