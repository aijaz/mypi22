import arcade
import os
from wordle import process_words, get_secret_word

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Wordle"
RADIUS = 150


# Classes
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


class Wordle(arcade.Window):
    """Main welcome window
    """
    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background window
        arcade.set_background_color(arcade.color.BLACK)

        # Set up the sprite lists
        self.max_guesses = 6
        self.cells = []
        self.create_cells()
        self.setup_cells()
        self.keys_by_char = {}

        # game variables
        self.current_guess = ""
        self.current_guess_number = 0
        self.game_over = False
        self.secret_word = get_secret_word()
        self.jump_cells = arcade.SpriteList()
        self.show_word = False

    def create_cells(self):
        for g in range(self.max_guesses):
            self.cells.append(arcade.SpriteList())

    def setup_cells(self):
        image_width = 56
        delta_x = image_width + 2
        delta_y = image_width + 2
        top_margin = 50
        center_x = int(SCREEN_WIDTH/2)

        top_left = Point(x=center_x - (delta_x * 2), y=SCREEN_HEIGHT - top_margin)
        current_location = top_left.clone()

        for g in range(self.max_guesses):
            current_location.x = top_left.x

            for c in range(5):
                cell = Cell(current_location)
                self.cells[g].append(cell)
                current_location.x += delta_x

            current_location.y -= delta_y

    def on_draw(self):
        # clear the screen
        self.clear()

        # draw each sprite list
        for r in range(self.max_guesses):
            self.cells[r].draw()

        if self.show_word:
            arcade.draw_text(self.secret_word,
                         SCREEN_WIDTH/2 - 40,
                         375,
                         arcade.color.WHITE,
                         18, bold=True)


    def on_update(self, delta_time: float):
        for r in range(self.max_guesses):
            self.cells[r].update()


    def shake(self):
        for cell in self.cells[self.current_guess_number]:
            cell.shake()



class Cell(arcade.Sprite):
    def __init__(self, location):
        super().__init__()
        blank = os.path.join("images", "cells", "blank", "BLANK.png")
        self.append_texture(arcade.load_texture(blank))
        self.set_texture(0)

        self.location = location.clone()
        self.center_x = self.location.x
        self.center_y = self.location.y
        self.is_moving = False
        self.direction_change = 0
        self.is_growing = False
        self.jump_state = 0
        self.success_animation_complete = False
        self.char = ''

    def set_char(self, char):
        gray = os.path.join("images", "cells", "gray", f"{char.upper()}.png")
        yellow = os.path.join("images", "cells", "yellow", f"{char.upper()}.png")
        green = os.path.join("images", "cells", "green", f"{char.upper()}.png")
        current = os.path.join("images", "cells", "current", f"{char.upper()}.png")

        self.textures = self.textures[:1]  # remove all but the first texture
        self.append_texture(arcade.load_texture(gray))
        self.append_texture(arcade.load_texture(yellow))
        self.append_texture(arcade.load_texture(green))
        self.append_texture(arcade.load_texture(current))
        self.set_texture(4)
        self.is_growing = True
        self.scale = 0.2
        self.char = char

    def clear(self):
        self.set_texture(0)
        self.textures = self.textures[:1]

    def set_color(self, result_status):
        if result_status == 'current':
            self.set_texture(4)
        elif result_status == 'Y':
            self.set_texture(3)
        elif result_status == '-':
            self.set_texture(2)
        else:
            self.set_texture(1)



# Main code entry point
if __name__ == "__main__":
    app = Wordle()
    arcade.run()
