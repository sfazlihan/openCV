import cv2, numpy

resim=cv2.imread("resim4.jpg")

buyukResim=cv2.pyrUp(resim)
kucukResim=cv2.pyrDown(resim)

print(resim.shape)
print(buyukResim.shape)
print(kucukResim.shape)

cv2.imshow("orijinal",resim)
cv2.imshow("Buyuk",buyukResim)
cv2.imshow("kucuk",kucukResim)

cv2.waitKey(0)
cv2.destroyAllWindows()

#matrisler ile bir image yazdırmak
MATRIS = numpy.zeros((500,500,3), dtype="uint8")
print(MATRIS)