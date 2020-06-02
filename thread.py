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
        global f
        f = set()

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

            sensitivity = 40
            f.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))

def detect_bulb(): 
        template2 = cv2.imread('C:\\Users\\E5-471G\\Desktop\\Detection\\sample4.png',0)
        w2, h2 = template2.shape[::-1]
        res2 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
        threshold2 = 0.6
        loc2 = np.where( res2 >= threshold2)

        global f2
        f2 = set()
        for pt in zip(*loc2[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0,255,0), 2)
            sensitivity = 45
            f2.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))

if __name__ == "__main__": 
        # creating thread 
        t1 = threading.Thread(target=detect_chr) 
        t2 = threading.Thread(target=detect_bulb) 

        # starting thread 1 
        t1.start() 
        # starting thread 2 
        t2.start() 

        # wait until thread 1 is completely executed 
        t1.join() 
        # wait until thread 2 is completely executed 
        t2.join() 

        cv2.imshow('res.png',img_rgb)
        hr_count = len(f)
        bulb_count = len(f2)
        print("Detections: ")
        print("Circuit Home Runs: "+str(hr_count))
        print("Number of Bulbs: "+str(bulb_count))
        # both threads completely executed 
        print("Done!") 
