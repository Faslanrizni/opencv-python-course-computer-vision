import os

import cv2
# img bluing use to remove noice im image


img = cv2.imread(os.path.join('.', 'cow-salt-peper.png'))
# cv2.imshow('img', img)
k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 20)
img_median_blur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
# this cow-salt-peper.png shows how this remove background notices

# k_size = 7 specifies that the kernel is a 7x7 matrix, meaning it covers a block of 7 pixels by 7 pixels around each
# pixel in the image. The kernel size must always be an odd number (e.g., 3, 5, 7) to ensure there is a central
# pixel, which allows the kernel to be symmetric. Odd sizes ensure that there is a central pixel in the kernel
# matrix, which allows it to be symmetrical. If the kernel size was even (e.g., 6x6), there would be no clear center,
# making it harder to apply the blurring effect consistently.