import numpy as np
import cv2
import pafy
import json
from framerate import Framerate
from ascii_image import Ascii_image
from cli_input import update_config

print('Start app')
with open('config.json') as config_file:
    config = json.load(config_file)
    config = update_config(config)

ASCII_SETTINGS = config['ascii']
SOURCE = config['source']
FPS = Framerate(config['output']['framerate'])
OUTPUT = config['output']


def get_youtube_source():
    url = SOURCE['youtubeUrl']
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    return best.url


def create_capture(source):
    cap = cv2.VideoCapture()
    cap.open(source)
    cap.set(3, SOURCE['width'])
    cap.set(4, SOURCE['height'])
    return cap


def exit_program():
    print('Gracefully exiting')
    cv2.destroyAllWindows()
    exit()


if SOURCE['youtubeUrl']:
    try:
        url = get_youtube_source()
        CAPTURE = create_capture(url)
    except OSError:
        print("Failure: can't find youtube source")
        exit_program()
elif SOURCE['localFile']:
    CAPTURE = create_capture(SOURCE['localFile'])
elif SOURCE['webcam']:
    CAPTURE = create_capture(0)
else:
    print("Failure: not defined video source")
    exit_program()


if not CAPTURE.isOpened():
    print("Failure: can't load video source")
    exit_program()

try:
    while(True):
        FPS.counter()

        size, frame = CAPTURE.read()
        if OUTPUT['mirror']:
            frame = cv2.flip(frame, 1)
        try:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        except cv2.error:
            print("Failure: lost connection to video source, please restart program")
            exit_program()

        ascii_image = Ascii_image(frame.tolist(), ASCII_SETTINGS)
        ascii_image.draw_on_console()

        if OUTPUT['show_window']:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
except KeyboardInterrupt:
    exit_program()
    # pass
