from email.mime import image

import  cv2
path= r"E:\MOVIES\ashish maurya\photoshop image\1234.jpg"
img=cv2.imread(path)
img= cv2.resize(img,(640,640))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()