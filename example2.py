import cv2

img = cv2.imread("indir.jpg")


# tüm fotoğraf üzerinde işlem yapar :img[:,:,2]=200		#b,g,r

img[25:100,25:100,1]=255	#belli pixeller içinde işlem yapmak
img[75:150,75:150,0]=255
img[125:200,125:200,2]=255




cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()