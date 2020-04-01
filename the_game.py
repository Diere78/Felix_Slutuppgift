import random
import math
import arcade
import os
import settings
from typing import cast
from object_classes import TurningCharacter, BulletSprite, WallSprite, CharacterSprite


class Game(arcade.Window):

    def __init__(self):
        super().__init__(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        self.set_fullscreen(True)
        
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.frame_count = 0

        self.game_over = False

        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.life_list = arcade.SpriteList()

        self.p1_score = 0
        self.p1_sprite = None
        self.p1_lives = 3
        self.p2_sprite = None
        self.p2_score = 0
        self.p2_lives = 3


    def startGame(self):

        self.frame_count = 0
        self.game_over = False

        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.life_list = arcade.SpriteList()

        self.p1_score = 0 
        self.p1_sprite = CharacterSprite("sprites/ladda_ned.png", settings.SCALE)
        self.all_sprites_list.append(self.p1_sprite)
        self.p1_lives = 3

        self.p2_score = 0
        self.p2_sprite = CharacterSprite("sprites/ladda_ned.png", settings.SCALE)
        self.all_sprites_list.append(self.p2_sprite)
        self.p2_lives = 3 

        cur_pos = 10

        for i in range(self.p1_lives):
            life = arcade.Sprite("sprites/life.png", settings.SCALE)
            life.center_x = cur_pos + life.width
            life.center_y = life.height
            cur_pos += life.width
            self.all_sprites_list.append(life)
            self.life_list.append(life)

        
        for i in range(self.p2_lives):
            life = arcade.Sprite("sprites/life.png", settings.SCALE)
            life.center_x = cur_pos - life.width
            life.center_y = life.height
            cur_pos += life.width
            self.all_sprites_list.append(life)
            self.life_list.append(life)

        """
        Skapa väggarna
        """

    def on_draw(self):

        arcade.start_render()    