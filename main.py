import cv2
import glob
import os

inputFolder='C:/Users/hp/OneDrive/Desktop/Leaf'
os.mkdir('C:/Users/hp/OneDrive/Desktop/Resize_300')

i=0
SIZE=300

for img in glob.glob(inputFolder+"/*.JPG"):
    image=cv2.imread(img)
    imgResized=cv2.resize(image,(SIZE,SIZE))
    cv2.imwrite('C:/Users/hp/OneDrive/Desktop/Resize_300/image%i.JPG' %i,imgResized)

    i+=1
    cv2.imshow('image',imgResized)
    cv2.waitKey(30)

cv2.destroyAllWindows()