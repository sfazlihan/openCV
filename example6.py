import cv2

resim1=cv2.imread("720.jpg")
resim2=cv2.imread("720_2.jpg")
print(resim1.shape)
print(resim2.shape)

topla=cv2.add(resim1,resim2)        #resimleri üstüste bindirmek
topla2=cv2.addWeighted(resim1,0.9,resim2,0.1,0)

cv2.imshow("topla",topla)
cv2.imshow("topla2",topla2)


cv2.waitKey(0)
cv2.destroyAllWindows()