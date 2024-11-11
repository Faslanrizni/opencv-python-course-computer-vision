import os

import cv2

base_dir = os.path.dirname(os.path.abspath(__file__))
# read video
video_path = os.path.join(base_dir, '..', 'data', 'Video.mp4')

video = cv2.VideoCapture(video_path)

# visualize video
# ret = True: Initializes ret to True. This variable indicates whether the video frame was read successfully.
# while ret:: This loop continues as long as ret is True.
# ret, frame = video.read(): Reads the next frame from the video:
# ret: A boolean indicating if the frame was read successfully (True if a frame was read, False if the video has ended).
# frame: The image data of the current frame.
ret = True

while ret:
    # ret =>
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)  # keep 40 s this frame

video.release()
cv2.destroyAllWindows()
