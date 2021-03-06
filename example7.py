import cv2

resim1=cv2.imread("720.jpg")

griResim=cv2.cvtColor(resim1, cv2.COLOR_BGR2GRAY)   # cv2.imread("720.jpg",0)

h,w,c=resim1.shape
h,w,=griResim.shape

print(h,w,c)


cv2.imshow("resim1",griResim)

cv2.waitKey(0)
cv2.destroyAllWindows()