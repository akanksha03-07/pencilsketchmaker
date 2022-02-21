import cv2
image = cv2.imread("cartoon.JPG")
grayimage=cv2.cvtColor (image,cv2.COLOR_BGR2GRAY)
invertedimage = 255-grayimage
blurredimage = cv2.GaussianBlur(invertedimage,(15,15),0)
invertedblur = 255-blurredimage
pencilsketch = cv2.divide (grayimage,invertedblur,scale=206.0)
cv2.imshow('final picture',pencilsketch)
cv2.imshow('black and white',grayimage)
cv2.imshow('original picture',image)

cv2.waitkey(0)
