import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    a=[]
    i=0
    if event == cv2.EVENT_LBUTTONDOWN:
        a=[x,y]
        print(a)
        i=i+1
        print(i)
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()