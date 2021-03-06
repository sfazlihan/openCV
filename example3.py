import cv2
 
img = cv2.imread("resim9.jpg")

kesit = img[50:200,300:500]
img[0:150,0:200]=kesit			#resim kopyalamak


img[200:250,300:350]=(0,255,255)	#belirli biryere sansür uygulamak




cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()