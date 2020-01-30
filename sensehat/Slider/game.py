from hat import Hat
from wall import Wall
from ball import Ball
import time
import random

class Game(Hat):
    def __init__(self):
        Hat.__init__(self)
        self.ball = Ball()
        self.walls = []  # list with active walls
        self.dist = 5  # distance between walls
        self.speed = 1  # speed of the walls
        self.gap = 5  # gap between walls
        self.cnt = -1  # counts the steps
        self.score = 0  # number of walls that went down
        self.alive = True  # The ball hasn't crashed into a wall
        self.main()


    def main(self):
        # self.instructions()
        self.intro()
        while self.alive:
            self.cnt += 1
            self.step()
            time.sleep(self.speed)


    def step(self):
        if self.cnt % self.dist == 0:  # check if a new wall should be created
            self.walls.append(self.new_wall())
        if self.walls[0].pos == 7:  # check if a wall should disappear
            self.walls[0].erase()
            self.walls.pop(0)
            self.score += 1
            if self.score % 10 == 0:
                self.levelup()
        self.survives()
        for w in (self.walls):  # move walls
            w.move()


    def levelup(self):
        if self.score % 3 == 0:  # smaller gap
            self.gap -= 1
        else:  # faster
            self.speed -= 0.1


    def survives(self):
        # check if ball runs into a wall
        if self.walls[0].pos == 6 and self.ball.pos >= self.walls[0].left and self.ball.pos <= self.walls[0].right:
            self.game_over()


    def new_wall(self):
        left = random.randint(0, self.gap)
        return Wall(left, left+7-self.gap)


    def instructions(self):
        msg = 'Avoid the walls by moving the joystick left and right.'
        self.sense.show_message(msg, 0.07, self.white) # instructions


    def intro(self):
        left, right, up, down = 1, 7, 1, 7
        while left != right:  # intro
            self.sense.clear(self.blue)  # set bg
            for i in range(left, right):
                for j in range(up, down):
                    self.sense.set_pixel(i, j, self.red)
            left += 1
            right -= 1
            up += 1
            down -= 1
            time.sleep(0.5)

        for i in range(4, 8):  # character moves down
            self.sense.clear(self.blue)
            self.sense.set_pixel(4, i, self.red)
            time.sleep(1)


    def game_over(self):
        self.alive = False
        msg = 'Score: ' + str(self.score)
        self.sense.show_message(msg, 0.07, self.red, self.yellow)  # outro
        self.sense.clear()


if __name__ == "__main__":
    game = Game()
