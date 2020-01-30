from sense_hat import SenseHat
import time

class Hat:
    def __init__(self):
        self.sense = SenseHat()

    def show_msg(self, msg, speed, color_a, color_bg):
        a = self.change_color(color_a)
        bg = self.change_color(color_bg)
        self.sense = SenseHat()
        self.sense.show_message(msg, speed, a, bg)

    def show_pattern(self, color_a, color_b):
        a = self.change_color(color_a)
        b = self.change_color(color_b)
        self.sense.clear(a)
        for i in range(0,8):
            for j in range(0,8):
                if (i+j) % 2 == 1:
                    self.sense.set_pixel(i, j, a)
                else:
                    self.sense.set_pixel(i, j, b)


    def turn_off(self, color=None):
        if color==None:
            self.sense.clear()
        else:
            self.sense.clear(color)

    def change_color(self, color):
        colors = {
            "red": (0, 255, 0),
            "blue": (0, 0, 255),
            "green": (0, 255, 0),
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "gray": (128, 255, 128)
            }
        return colors[color]
    

if __name__ == "__main__":
    hat = Hat()
    orange = (255, 129, 16)
    blue = (0, 207, 255)
    msg = 'Hola mama!'
    hat.show_pattern("gray", "black")
    # hat.show_msg(msg, 0.1, "blue", "red")
    time.sleep(10)
    hat.turn_off()
