# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('C:\\Users\\E5-471G\\Desktop\\Detection\\plan3.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

def detect_chr(): 
        template = cv2.imread('C:\\Users\\E5-471G\\Desktop\\Detection\\hr.png',0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.6
        loc = np.where( res >= threshold)
        global hr_count
        f = set()

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

            sensitivity = 40
            f.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))
        hr_count = len(f)

def detect_bulb(): 
        template2 = cv2.imread('C:\\Users\\E5-471G\\Desktop\\Detection\\sample4.png',0)
        w2, h2 = template2.shape[::-1]
        res2 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
        threshold2 = 0.56
        loc2 = np.where( res2 >= threshold2)

        global bulb_count
        f2 = set()
        for pt in zip(*loc2[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0,255,0), 2)
            sensitivity = 45
            f2.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))
        bulb_count = len(f2)
            
def detect_wmb():

        template3 = cv2.imread('C:\\Users\\E5-471G\\Desktop\\Detection\\wmb.png',0)
        w3, h3 = template3.shape[::-1]
        res3 = cv2.matchTemplate(img_gray,template3,cv2.TM_CCOEFF_NORMED)
        threshold3 = 0.8
        loc3 = np.where( res3 >= threshold3)
        
        template4 = cv2.imread('C:\\Users\\E5-471G\\Desktop\\Detection\\wmb2.png',0)
        w4, h4 = template4.shape[::-1]
        res4 = cv2.matchTemplate(img_gray,template4,cv2.TM_CCOEFF_NORMED)
        threshold4 = 0.8
        loc4 = np.where( res4 >= threshold4)
        
        template5 = cv2.imread('C:\\Users\\E5-471G\\Desktop\\Detection\\wmb3.png',0)
        w5, h5 = template5.shape[::-1]
        res5 = cv2.matchTemplate(img_gray,template5,cv2.TM_CCOEFF_NORMED)
        threshold5 = 0.8
        loc5 = np.where( res5 >= threshold5)

        
        f3 = set()
        f4 = set()
        f5 = set()
        
        for pt in zip(*loc3[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w3, pt[1] + h3), (255,140,0), 2)
            sensitivity = 45
            f3.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))
            
        for pt in zip(*loc4[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w4, pt[1] + h4), (255,140,0), 2)
            sensitivity = 45
            f4.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))
            
        for pt in zip(*loc5[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w5, pt[1] + h5), (255,140,0), 2)
            sensitivity = 45
            f5.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))

        global wmb_count
        wmb_count = len(f5)+len(f4)+len(f3)
            
if __name__ == "__main__": 
        # creating thread 
        t1 = threading.Thread(target=detect_chr) 
        t2 = threading.Thread(target=detect_bulb)
        t3 = threading.Thread(target=detect_wmb)

 
        t1.start() 
        t2.start()
        t3.start()
        
        t1.join()
        t2.join()
        t3.join()

        cv2.imshow('res.png',img_rgb)
         
        
        
        
        print("Detections: ")
        print("Circuit Home Runs: "+str(hr_count))
        print("Number of Bulbs: "+str(bulb_count))
        print("Wall Mounted Bulbs: "+str(wmb_count))
        # both threads completely executed 
        print("Done!") 
