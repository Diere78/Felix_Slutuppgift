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
        self.drag = 0.05
        self.thrust = 0
        self.speed = 0
        self.max_speed = 4
        self.respawn()

    def respawn(self):

        self.respawning = 1
        #Kommer ändras senare så de två spelarna inte spawnar på samma plats.
        self.center_x = settings.SCREEN_WIDTH / 2
        self.center_y = settings.SCREEN_HEIGHT / 2
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
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x < settings.LEFT_LIMIT:
            self.center_x = settings.RIGHT_LIMIT
        if self.center_x > settings.RIGHT_LIMIT:
            self.center_x = settings.LEFT_LIMIT
        if self.center_y > settings.TOP_LIMIT:
            self.center_y = settings.BOTTOM_LIMIT
        if self.center_y < settings.BOTTOM_LIMIT:
            self.center_y = settings.TOP_LIMIT

        """ Call the parent class. """
        super().update()


class WallSprite(arcade.Sprite):

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.size = 0
"""
Fixar den här klassen senare, när jag listat ut exakt vad jag vill göra med den,
och när jag hittat passande sprites
"""


class BulletSprite(TurningSprite):

    def update(self):
        super().update()
        if self.center_x < -100 or self.center_x > 1500 or \
                self.center_y > 1100 or self.center_y < -100:
            self.remove_from_sprite_lists()

"""
En power up klass
"""