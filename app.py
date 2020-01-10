import numpy as np
import cv2
import os
from time import sleep
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

NEGATIVE_CAPTURE = False

ASCII_GRADIENT = [
    '$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w',
    'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j',
    'f', 't', '/', "/", '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>',
    'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

if not NEGATIVE_CAPTURE:
    ASCII_GRADIENT.reverse()

GRADIENT_SCALE_FACTOR = 256 / len(ASCII_GRADIENT)

# def half_size_array(two_d_array):
#     two_d_array[1::2]
#     for row in two_d_array:
#         row[1::2]
#     return two_d_array

# def cls():
#     os.system('cls' if os.name=='nt' else 'clear')

# os.system("mode con cols=80 lines=30")

while(True):
    # rows1, columns1 = os.popen('stty size', 'r').read().split()
    # print("\x1b[8;100;100")
    sleep(0.05)
    os.system('clear')
    # TODO: Find a better solution, or perhaps use cv solution if possible
    # if keyboard.is_pressed('z'):
    #     print('Attempt to exit')
    #     break

    # Capture frame-by-frame
    size, frame = CAPTURE.read()
    frame = cv2.flip(frame, 1)

    # Operations on each frame
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except cv2.error as e:
        print('oopsie camera not found', e)
        CAPTURE.release()
        cv2.destroyAllWindows()
        exit()

    ascii_image = gray.tolist()
    del ascii_image[::2]
    del ascii_image[::2]

    for row in ascii_image:
        del row[::2]

    del ascii_image[::2]
    for row in ascii_image:
        del row[::2]

    del ascii_image[::2]
    for row in ascii_image:
        del row[::2]

    # breakpoint()
    for row in ascii_image:
        output_text_line = ''
        for column in row:
            grayscale_value = int(round(column / GRADIENT_SCALE_FACTOR))
            if grayscale_value > len(ASCII_GRADIENT) - 1:
                grayscale_value = len(ASCII_GRADIENT) - 1
            if grayscale_value < 0:
                grayscale_value = 0

            output_text_line = output_text_line + \
                ASCII_GRADIENT[grayscale_value]
        # stdout.write(output_text_line + '\n')
        print(output_text_line)
    # stdout.flush()
    # breakpoint()

    if show_capture:
        cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('Gracefully exiting')
CAPTURE.release()
cv2.destroyAllWindows()
