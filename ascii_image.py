import os


class Ascii_image:

    def __init__(self,
                 ascii_image,
                 fps,
                 ascii_image_size='small',
                 NEGATIVE_CAPTURE=True):
        self.ASCII_GRADIENT = [
            '$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h',
            'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C',
            'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f',
            't', '/', "/", '|', '(', ')', '1', '{', '}', '[', ']', '?', '-',
            '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"',
            '^', '`', "'", '.', ' ']
        self.NEGATIVE_CAPTURE = NEGATIVE_CAPTURE
        self.GRADIENT_SCALE_FACTOR = 256 / len(self.ASCII_GRADIENT)
        self.ascii_image = ascii_image
        self.ascii_image_size = ascii_image_size
        self.__inverse_ascii_gradient()
        self.resize_image()

    # █
    def draw_on_console(self):
        os.system('clear')
        for row in self.ascii_image:
            output_text = ''
            for column in row:
                gray_value = int(round(column / self.GRADIENT_SCALE_FACTOR))
                if gray_value > len(self.ASCII_GRADIENT) - 1:
                    gray_value = len(self.ASCII_GRADIENT) - 1
                if gray_value < 0:
                    gray_value = 0
                output_text = output_text + self.ASCII_GRADIENT[gray_value]
            print(output_text)

    def resize_image(self):
        self.__resize_height_to_half()
        if self.ascii_image_size == 'small':
            self.__resize_all_to_half()
        self.__resize_all_to_half()
        self.__resize_all_to_half()

    def __resize_height_to_half(self):
        del self.ascii_image[::2]

    def __resize_all_to_half(self):
        del self.ascii_image[::2]
        for row in self.ascii_image:
            del row[::2]

    def __inverse_ascii_gradient(self):
        if self.NEGATIVE_CAPTURE:
            self.ASCII_GRADIENT.reverse()
