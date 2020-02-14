import numpy as np
import cv2
import pafy
from framerate import Framerate
from ascii_image import Ascii_image


print('Start app')

INPUT_SCREEN = {
    'w': 640,
    'h': 480
}

youtube = True

if youtube:
    url = "https://www.youtube.com/watch?v=ojdbDYahiCQ&list=PLwHzkHf4F9UJ3xuFTuoBXcWHaciYH8g8Q&index=24&t=0s"
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")

    CAPTURE = cv2.VideoCapture()
    CAPTURE.open(best.url)
else:
    CAPTURE = cv2.VideoCapture(0)


CAPTURE.set(3, INPUT_SCREEN['w'])
CAPTURE.set(4, INPUT_SCREEN['h'])
show_capture = True
fps = Framerate(30)

while(True):
    fps.counter()

    try:
        size, frame = CAPTURE.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except cv2.error as e:
        print('Failure: webcam not found', e)
        CAPTURE.release()
        cv2.destroyAllWindows()
        exit()

    ascii_image = Ascii_image(frame.tolist(), 1)
    ascii_image.draw_on_console()

    if show_capture:
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('Gracefully exiting')
CAPTURE.release()
cv2.destroyAllWindows()
