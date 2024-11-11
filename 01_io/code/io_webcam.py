import cv2

# read webcam
webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit()
# visualize webcam

while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

# It reads a single frame from the video stream.
# ret is a boolean value that indicates whether the frame was read successfully (True) or not (False).
# frame is the actual image (frame) captured from the webcam.
# Why check ret?
# If ret is False, it means the frame could not be captured, which could happen if the webcam is not properly initialized or there is an issue with the device.