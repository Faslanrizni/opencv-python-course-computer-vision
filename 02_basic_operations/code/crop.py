# crop
import os

import cv2

base_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(base_dir, '..', 'data', 'bird.jpeg')

img = cv2.imread(image_path)

print(img.shape)

cropped_img = img[0:150, 0:100]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
