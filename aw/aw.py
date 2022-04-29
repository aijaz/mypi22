import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Wordle"

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

