import cv2, numpy

kamera=cv2.VideoCapture(0)  #0-pcnin kamerası, 1-USB kamera, 2-video yolu

while True:
    ret,goruntu=kamera.read()
    
    cv2.imshow("Canlı",goruntu)
    if (cv2.waitKey(1)) & 0xFF==ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()