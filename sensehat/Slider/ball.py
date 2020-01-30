from hat import Hat

class Ball(Hat):
    def __init__(self, pos=4):
        Hat.__init__(self)
        self.pos = pos
        self.sense.stick.direction_right = self.move_right
        self.sense.stick.direction_left = self.move_left

    def move_right(self):
        if self.pos < 7:
            self.sense.set_pixel(self.pos, 7, self.blue)
            self.pos += 1
            self.sense.set_pixel(self.pos, 7, self.red)

    def move_left(self):
        if self.pos > 0:
            self.sense.set_pixel(self.pos, 7, self.blue)
            self.pos -= 1
            self.sense.set_pixel(self.pos, 7, self.red)
