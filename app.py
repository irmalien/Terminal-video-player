import numpy as np
import cv2
import pafy
import json
from framerate import Framerate
from ascii_image import Ascii_image

print('Start app')
with open('examples/example_local_file_2/config.json') as config_file:
    config = json.load(config_file)

SHOW_VIDEO = config['output']['show_video_window']
FPS = Framerate(config['output']['framerate'])
ASCII_SETTINGS = config['ascii']
MIRROR_VIDEO = config['output']['mirror']


def get_youtube_source():
    url = config['source']['youtubeUrl']
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    return best.url


def create_capture(source):
    cap = cv2.VideoCapture()
    cap.open(source)
    cap.set(3, config['source']['width'])
    cap.set(4, config['source']['height'])
    return cap


def exit_program():
    print('Gracefully exiting')
    cv2.destroyAllWindows()
    exit()


if config['source']['youtubeUrl']:
    try:
        url = get_youtube_source()
        CAPTURE = create_capture(url)
    except OSError:
        exit_program()
elif config['source']['localFile']:
    CAPTURE = create_capture(config['source']['localFile'])
elif config['source']['webcam'] == 0:
    CAPTURE = create_capture(0)
else:
    raise NameError("Failure: not defined video source")
    exit_program()

try:
    if not CAPTURE.isOpened():
        raise NameError("Failure: can't load video source")
except:
    exit_program()

while(True):
    FPS.counter()

    size, frame = CAPTURE.read()
    if MIRROR_VIDEO:
        frame = cv2.flip(frame, 1)
    try:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except:
        raise NameError(
            "Failure: lost connection to video source, please restart program")
        exit_program()

    ascii_image = Ascii_image(frame.tolist(), ASCII_SETTINGS)
    ascii_image.draw_on_console()

    if SHOW_VIDEO:
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

exit_program()
