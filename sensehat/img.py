from sense_hat import SenseHat
from PIL import Image
import time

class Hat:1
    def __init__(self):
        self.sense = SenseHat()

    def create_thumbnail(self, f):
        name, path = self.get_info(f)
        img = Image.open(f)
        th = img.resize((8, 8))
        res = path + name + '_thumbnail.jpg'
        th.save(res)
        return res

    def show_img(self, img):
        print(img)
        self.sense.load_image(img)


    def get_info(self, f):
        name = ''
        path = ''
        i = len(f) - 1
        while i >= 0:
            if f[i] == '.':
                i -= 1
                while f[i] != '/':
                    name = f[i] + name
                    i -= 1
                while i >= 0:
                    path = f[i] + path
                    i -= 1
            i -= 1
        return (name, path)

    def turn(self, color=None):
        if color==None:
            self.sense.clear()
        else:
            self.sense.clear(color)
        

if __name__ == "__main__":
    sense = Hat()
    lion = "../images/cross.jpeg"
    fname = sense.create_thumbnail(lion)
    sense.show_img(fname)
    time.sleep(10)
    sense.turn()
