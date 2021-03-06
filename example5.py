import cv2
 
img = cv2.imread("resim8.jpg")

cv2.rectangle((img),(300,100),(100,300),[255,255,50],2)     #rectangle((resim),(sol alt köşe x noktası),(sağ üst köşe y noktası),[renk],kalınlık)
cv2.rectangle((img),(100,500),(500,300),[255,255,50],2)     #rectangle((resim),(sol alt köşe x noktası),(sağ üst köşe y noktası),[renk],kalınlık)
cv2.rectangle((img),(600,250),(450,300),[255,255,50],2)     #rectangle((resim),(sol alt köşe x noktası),(sağ üst köşe y noktası),[renk],kalınlık)



cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()