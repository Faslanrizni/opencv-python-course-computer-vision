# resizing
import os

import cv2
base_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(base_dir, '..', 'data', 'bird.jpeg')


img = cv2.imread(image_path)

resized_img = cv2.resize(img, (640, 640))

print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
