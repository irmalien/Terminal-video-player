import os


class Ascii_image:

    def __init__(self,
                 image_arr,
                 NEGATIVE_CAPTURE=True):
        self.ASCII_GRADIENT = self.__ascii_gradient_1()
        self.NEGATIVE_CAPTURE = NEGATIVE_CAPTURE
        self.GRADIENT_SCALE_FACTOR = 256 / len(self.ASCII_GRADIENT)
        self.console = {
            'rows': int(os.popen('stty size', 'r').read().split()[0]),
            'columns': int(os.popen('stty size', 'r').read().split()[1])
        }
        self.image_arr = image_arr
        self.ascii_arr = []
        self.__inverse_ascii_gradient()
        self.__resize_image()

    def draw_on_console(self):
        self.__convert_to_ascii_arr()
        self.__add_borders()
        self.__center_in_console()
        os.system('clear')
        self.__output_text_to_console()

    # private

    def __add_borders(self):
        horisontal_line = []
        height = len(self.ascii_arr) - 1
        width = len(self.ascii_arr[0]) - 1
        for column in self.ascii_arr[0]:
            horisontal_line.append('█')
        self.ascii_arr[0] = horisontal_line
        self.ascii_arr[height] = horisontal_line

        for i in range(len(self.ascii_arr)):
            self.ascii_arr[i][0] = '█'
            self.ascii_arr[i][1] = '█'
            self.ascii_arr[i][width] = '█'
            self.ascii_arr[i][width - 1] = '█'

    def __ascii_gradient_1(self):
        ascii_list = [
            '$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h',
            'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C',
            'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f',
            't', '1', '(', ')', '{', '}', '[', ']', '/', "/", '|', '?', '<', '>',
            'i', '!', 'l', 'I', '-', '_', '+', '~', ';', ':', ',', '"',
            '^', '`', "'", '.', ' ', ' ', ' ']
        return ascii_list

    def __ascii_gradient_2(self):
        ascii_string = 'ÆÑÊŒØMÉËÈÃÂWQBÅæ#NÁþEÄÀHKRŽœXgÐêqÛŠÕÔA€ßpmãâG¶øðé8ÚÜ$ëdÙýèÓÞÖåÿÒb¥FDñáZPäšÇàhû§ÝkŸ®S9žUTe6µOyxÎ¾f4õ5ôú&aü™2ùçw©Y£0VÍL±3ÏÌóC@nöòs¢u‰½¼‡zJƒ%¤Itocîrjv1lí=ïì<>i7†[¿?×}*{+()/»«•¬|!¡÷¦¯—^ª„”“~³º²–°­¹‹›;:’‘‚’˜ˆ¸…·¨´`'

    def __ascii_gradient_3(self):
        ascii_string = '@%#*+=-:.'
        return [char for char in ascii_string]

    def __ascii_gradient_4(self):
        ascii_string = '█▓▒░ '
        return [char for char in ascii_string]

    def __ascii_gradient_5(self):
        ascii_string = '████▟▜▛▙▞▚▞▚▝▘▗▖    '
        return [char for char in ascii_string]

    def __center_in_console(self):
        top_margin = int(
            (self.console['rows'] - len(self.ascii_arr)) / 2) - 1
        ver_margin = int(
            (self.console['columns'] - len(self.ascii_arr[0])) / 2)
        # Generate margins on left and right
        for col in range(ver_margin):
            for row in range(len(self.ascii_arr) - 1):
                self.ascii_arr[row].append(' ')
                self.ascii_arr[row].insert(0, ' ')
        # Generate margins on top and bottom
        for row in range(top_margin):
            new_line = []
            for col in range(len(self.ascii_arr[0])):
                new_line.append(' ')
            self.ascii_arr.append(new_line)
            self.ascii_arr.insert(0, new_line)

    def __convert_to_ascii_arr(self):
        self.ascii_arr = []
        for row in self.image_arr:
            ascii_row = []
            for column in row:
                gray_value = int(round(column / self.GRADIENT_SCALE_FACTOR))
                if gray_value > len(self.ASCII_GRADIENT) - 1:
                    gray_value = len(self.ASCII_GRADIENT) - 1
                if gray_value < 0:
                    gray_value = 0
                ascii_row.append(self.ASCII_GRADIENT[gray_value])
            self.ascii_arr.append(ascii_row)

    def __inverse_ascii_gradient(self):
        if self.NEGATIVE_CAPTURE:
            self.ASCII_GRADIENT.reverse()

    def __output_text_to_console(self):
        for row in self.ascii_arr:
            output_text = ''
            for column in row:
                output_text = output_text + column
            print(output_text)

    def __resize_image(self):
        self.__resize_height_to_half()
        while (len(self.image_arr[0])) > self.console['columns']:
            self.__resize_all_to_half()

    def __resize_height_to_half(self):
        del self.image_arr[::2]

    def __resize_all_to_half(self):
        del self.image_arr[::2]
        for row in self.image_arr:
            del row[::2]
