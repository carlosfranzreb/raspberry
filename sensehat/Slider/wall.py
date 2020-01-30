from hat import Hat

class Wall(Hat):
    def __init__(self, left, right):
        Hat.__init__(self)
        self.left = left ## left border
        self.right = right  # right border
        self.pos = 0 # wall starts up
        self.draw()

    def draw(self):
        for i in range(8):
            if i < self.left or i > self.right:
                self.sense.set_pixel(i, self.pos, self.green)

    def erase(self):
        for i in range(8):
            if i < self.left or i > self.right:
                self.sense.set_pixel(i, self.pos, self.blue)

    def move(self):
        self.erase()
        self.pos += 1
        if self.pos >= 0:
            self.draw()
        return False
