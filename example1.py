import cv2
import numpy as np
image1 = cv2.imread("indir.jpg")
image2 = cv2.imread("resim1.jpg",0)

#cv2.imwrite("cv_gray.png",image1)

print("image1 boyutu : ",image1.size)
print("image2 boyutu : ",image2.size)
print("image1 özellikleri : ",image1.shape)
print("image2 özellikleri : ",image2.shape)
print("image1 türü : ",image1.dtype)
print("image2 türü : ",image2.dtype)
print(image1[(100,200)])


image1[100,100]=[0,0,255]

for i in range(100):
    image1[i,i]=[0,0,255]





cv2.imshow("cv",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()