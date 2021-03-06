import cv2

kamera=cv2.VideoCapture(0)  #0-pcnin kamerası, 1-USB kamera, 2-video yolu

while True:
    k,goruntu=kamera.read()
    
    
    cv2.putText(goruntu,"FAZLIHAN",(100,400),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    
    cv2.imshow("Canlı",goruntu)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()