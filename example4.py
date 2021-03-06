import cv2
 
img = cv2.imread("resim10.jpg")

aynalama=cv2.copyMakeBorder(img,200,200,200,200,cv2.BORDER_REFLECT) #copyMakeBorder(src, top, bottom, left, right, borderType)
uzatma=cv2.copyMakeBorder(img,200,200,200,200,cv2.BORDER_REPLICATE) #copyMakeBorder(src, top, bottom, left, right, borderType)
tekrarlama=cv2.copyMakeBorder(img,200,200,200,200,cv2.BORDER_WRAP) #copyMakeBorder(src, top, bottom, left, right, borderType)
sarma=cv2.copyMakeBorder(img,75,75,75,75,cv2.BORDER_CONSTANT,value=(25,25,75)) #copyMakeBorder(src, top, bottom, left, right, borderType, value(b,g,r))

cv2.imshow("image",img)
cv2.imshow("uzatma",uzatma)
cv2.imshow("tekrarlama",tekrarlama)
cv2.imshow("sarma",sarma)

cv2.waitKey(0)
cv2.destroyAllWindows()