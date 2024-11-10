import os

import cv2

# read image

# Construct the image path
base_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the directory of the current script
print(base_dir)
image_path = os.path.join(base_dir, '..', 'data', 'bird.jpeg')  # Navigate to the 'data' folder

img = cv2.imread(image_path)

# write image

cv2.imwrite(os.path.join(base_dir, '..', 'data', 'bird_out.jpeg'), img)

# visualize image

cv2.imshow('image', img)
cv2.waitKey(0)
