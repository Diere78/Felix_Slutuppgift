import random
import math
import arcade
import os
import settings


class TurningSprite(arcade.Sprite):
    "Class that turns the sprite to the direction it is moving in"
    def update(self):
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))


class CharacterSprite(arcade.Sprite):

    def __init__(self, filename, scale):

        super().__init__(filename, scale)
        self.speed = 0
        self.respawn()

    def respawn(self):

        self.respawning = 1
        self.angle = 0

    def update(self):
        """
        Update our position and other particulars.
        """
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y

        super().update()


class WallSprite(arcade.Sprite):

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.size = 0


class BulletSprite(TurningSprite):

    def update(self):
        super().update()
        if self.center_x < -100 or self.center_x > 1500 or \
                self.center_y > 1100 or self.center_y < -100:
            self.remove_from_sprite_lists()
