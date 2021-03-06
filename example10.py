import cv2 as cv
import numpy as np

MATRIS = np.zeros((500,500,3), dtype="uint8")


cv.line(MATRIS,(100,200),(300,100),(125,255,0),3)
cv.line(MATRIS,(100,200),(300,200),(125,255,0),3)
cv.line(MATRIS,(300,100),(300,200),(125,255,0),3)

cv.circle(MATRIS,(100,200),40,(0,0,255),3)

cv.putText(MATRIS,"OpenCV",(100,400),cv.FONT_HERSHEY_COMPLEX,3,(0,255,0),3)
cv.line(MATRIS,(100,405),(470,405),(255,125,0),3)

cv.waitKey(0)
cv.destroyAllWindows()