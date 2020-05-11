import arcade
import random
import math
import os
from typing import cast
from the_game import Game


def main():
    window = Game()
    window.startGame()
    arcade.run()

if __name__ == "__main__":
    main()