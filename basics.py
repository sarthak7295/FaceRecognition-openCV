import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('dog.png',0) #numpy array
plt.imshow(img, cmap='gray', interpolation='bicubic')
#cv2 reads color img in BGR and plt displays in RGB so it is not easy to display colored image
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


################################
# code for colored image
################################
img = cv2.imread('dog.png')
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()
cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()



###############################
# Video capture webcam
###############################

cap = cv2.VideoCapture(0)     #for camera

cap = cv2.VideoCapture('vtest.avi')    for video file

ret, frame = cap.read()   # ret is boolean true if frame is captured correctly
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


###############not going for video writer now since i dont need it right now


############################
#Drawing
############################

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px

cv2.line(img,(0,0),(511,511),(255,0,0),5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('line image',img)
cv2.waitKey(0)



##################
# no need for mouse drawing basics
###############

px = img[100,100]
print px
[157 166 200]    BGR

# accessing only blue pixel
blue = img[100,100,0]   last digit is BRG so BLue
print blue
157               !!!!!!!!!!!!!!!!!!np arrqay is unint8 so max is 255!!!!
                    #####so if you add more than 255 it becomes modulo like 250+10 = 260 % 256 = 4   numpy add
                    you can cv.add for saturaton max will be 255 only



dst = cv2.addWeighted(img1,0.7,img2,0.3,0) weighted addition  merge like overlap
last is constant addition



#############
# we can use bit wise operation on images, not doing it but keeping for further reference
#############
#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html#image-arithmetics
# Load two images
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()