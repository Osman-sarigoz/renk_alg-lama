from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2
import math
def main():
    
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate =32
    rawCapture=PiRGBArray(camera,size = (640,480))
 
    time.sleep(0.1)
    #kırmızı renk değerlikleri
    alt_deger=np.array([0,0,190])
    ust_deger=np.array([100,100,255])
    #mavi için
    alt_deger1=np.array([190,0,0])
    ust_deger1=np.array([255,100,100])
    #yeşil renk değerlikleri
    alt_deger_1=np.array([0,190,0])
    ust_deger_1=np.array([100,255,100])
 
    for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
           
        frame = frame.array
        #cv2.imshow("Kamera ilk Ekran",frame)
        # kırmızı için
        filtre1=cv2.inRange(frame,alt_deger,ust_deger)
        #cv2.imshow("Kırmızı Renk Aralıkları",filtre1)
        filtre1=cv2.GaussianBlur(filtre1,(3,3),2)
        #cv2.imshow("Kırmızı Gauss Filtresi",filtre1)
        filtre1 = cv2.dilate(filtre1,np.ones((5,5),np.uint8))
        #cv2.imshow("Kırmızı Dilate kod",filtre1)
        filtre1 = cv2.erode(filtre1,np.ones((5,5),np.uint8))
        #cv2.imshow("Kırmızı Erode kod",filtre1)
        intRows,intColums = filtre1.shape
        circles = cv2.HoughCircles(filtre1,cv2.HOUGH_GRADIENT,5,intRows/4)
        if circles is not None:#kırmızı için
             for circle in circles[0]:
                 x,y,radius=circle
                 cv2.circle(frame,(x,y),3,(255,255,255),-1)
                 cv2.circle(frame,(x,y),radius,(0,0,255),3)
        
        # mavi için
        filtre2=cv2.inRange(frame,alt_deger1,ust_deger1)
        filtre2=cv2.GaussianBlur(filtre2,(3,3),2)
        filtre2 = cv2.dilate(filtre2,np.ones((5,5),np.uint8))
        filtre2 = cv2.erode(filtre2,np.ones((5,5),np.uint8))
        intRows,intColums = filtre2.shape
        circlessari = cv2.HoughCircles(filtre2,cv2.HOUGH_GRADIENT,5,intRows/4)
        if circlessari is not None:
             for circle in circlessari[0]:
                 x,y,radius=circle
                 cv2.circle(frame,(x,y),3,(255,255,255),-1)
                 cv2.circle(frame,(x,y),radius,(255,0,0),3)         
        
        #yeşil için
        filtre2=cv2.inRange(frame,alt_deger_1,ust_deger_1)
        filtre2=cv2.GaussianBlur(filtre2,(3,3),2)
        filtre2 = cv2.dilate(filtre2,np.ones((5,5),np.uint8))
        filtre2 = cv2.erode(filtre2,np.ones((5,5),np.uint8))
        intRows,intColums = filtre2.shape
        circless = cv2.HoughCircles(filtre2,cv2.HOUGH_GRADIENT,5,intRows/4)
        if circless is not None:
            for circle in circless[0]:
                x,y,radius=circle
                cv2.circle(frame,(x,y),3,(255,255,255),-1)
                cv2.circle(frame,(x,y),radius,(0,255,0),3)
                

        cv2.imshow("Ekran",frame)
 
        key=cv2.waitKey(1)&0xFF
 
        rawCapture.truncate(0)
 
        if key==ord("q"):
            cv2.destroyAllWindows()
            camera.close()
            break
 
if __name__ == "__main__":
    main()


