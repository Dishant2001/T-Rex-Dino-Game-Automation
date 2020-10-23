from pil import ImageGrab
import cv2
import numpy as np
import time
import pyautogui
time.sleep(2) 
low=np.array([0,0,0])
high=np.array([50,50,150])
while True:
    img=np.array(ImageGrab.grab(bbox=(672,400,1400,550)))
    cv2.circle(img,(8,155),5,(0,0,255),3)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,low,high)
    conts,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for cont in conts:
        area=cv2.contourArea(cont)
        if area>100:
            cv2.drawContours(img,cont,-1,(0,255,0),2)
            M=cv2.moments(cont)
            cx1=int(M["m10"]/M["m00"])
            cy1=int(M["m01"]/M["m00"])
            cv2.circle(img,(cx1,cy1),5,(0,0,255),1)
            if cx1-15<=110:
                if cy1>=200:
                    pyautogui.keyDown('Down')
                    print('duck')
                else:
                    pyautogui.keyDown('Up')
                    print('jump')
    cv2.imshow("_",img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
x,y=pyautogui.position()
print(cx1,cy1)

