import numpy as np
import cv2
import os
from time import sleep
from framerate import Framerate
from ascii_image import Ascii_image
# import keyboard
# from sys import stdout

print('program started')

INPUT_SCREEN = {
    'w': 640,
    'h': 480
}

CAPTURE = cv2.VideoCapture(0)
CAPTURE.set(3, INPUT_SCREEN['w'])
CAPTURE.set(4, INPUT_SCREEN['h'])
show_capture = True
fps = Framerate(30)

while(True):
    fps.counter()
    console = {
        'rows': os.popen('stty size', 'r').read().split()[0],
        'columns': os.popen('stty size', 'r').read().split()[0]
    }
    size, frame = CAPTURE.read()
    frame = cv2.flip(frame, 1)

    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except cv2.error as e:
        print('oopsie camera not found', e)
        CAPTURE.release()
        cv2.destroyAllWindows()
        exit()

    ascii_image = Ascii_image(gray.tolist(),
                              fps.actual_fps,
                              'large')

    ascii_image.draw_on_console()

    if show_capture:
        cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('Gracefully exiting')
CAPTURE.release()
cv2.destroyAllWindows()
