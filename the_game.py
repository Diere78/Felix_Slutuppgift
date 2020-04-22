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
            self.p1_life_list.append(life)

        
        for i in range(self.p2_lives):
            life = arcade.Sprite("sprites/life.png", settings.SCALE)
            life.center_x = cur_pos - life.width
            life.center_y = life.height
            cur_pos += life.width
            self.all_sprites_list.append(life)
            self.p2_life_list.append(life)

        """
        Skapa väggarna
        """

    def on_draw(self):

        arcade.start_render() 

        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = f"Player 1 Score: {self.p1_score}"
        arcade.draw_text(output, 10, 70, arcade.color.WHITE, 13)

        output = f"Player 2 Count: {(self.p2_score)}"
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 13)   

    def on_key_press(self, symbol, modifiers):

        if not self.p1_sprite.respawning and symbol == arcade.key.SPACE:
            bullet_sprite = BulletSprite("images/laserBlue01.png", settings.SCALE)
            bullet_sprite.guid = "Bullet"

            bullet_speed = 30
            bullet_sprite.change_y = \
                math.cos(math.radians(self.p1_sprite.angle)) * bullet_speed
            bullet_sprite.change_x = \
                -math.sin(math.radians(self.p1_sprite.angle)) \
                * bullet_speed

            bullet_sprite.center_x = self.p1_sprite.center_x
            bullet_sprite.center_y = self.p1_sprite.center_y
            bullet_sprite.update()

            self.all_sprites_list.append(bullet_sprite)
            self.bullet_list.append(bullet_sprite)
        
        if not self.p2_sprite.respawning and symbol == arcade.key.E:
            bullet_sprite = BulletSprite("images/laserBlue01.png", settings.SCALE)
            bullet_sprite.guid = "Bullet"

            bullet_speed = 30
            bullet_sprite.change_y = \
                math.cos(math.radians(self.p2_sprite.angle)) * bullet_speed
            bullet_sprite.change_x = \
                -math.sin(math.radians(self.p2_sprite.angle)) \
                * bullet_speed

            bullet_sprite.center_x = self.p2_sprite.center_x
            bullet_sprite.center_y = self.p2_sprite.center_y
            bullet_sprite.update()

            self.all_sprites_list.append(bullet_sprite)
            self.bullet_list.append(bullet_sprite)

        elif symbol == arcade.key.LEFT:
            self.p1_sprite.change_angle = 3
        elif symbol == arcade.key.RIGHT:
            self.p1_sprite.change_angle = -3
        elif symbol == arcade.key.UP:
            self.p1_sprite.thrust = 0.2
        elif symbol == arcade.key.DOWN:
            self.p1_sprite.thrust = -0.2
        elif symbol == arcade.key.ESCAPE:
            exit()
        elif symbol == arcade.key.A:
            self.p2_sprite.change_angle = 3
        elif symbol == arcade.key.D:
            self.p2sprite.change_angle = -3
        elif symbol == arcade.key.W:
            self.p2_sprite.thrust = 0.1
        elif symbol == arcade.key.S:
            self.p2_sprite.thrust = -0.1

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            self.p1_sprite.change_angle = 0
        elif symbol == arcade.key.RIGHT:
            self.p1_sprite.change_angle = 0
        elif symbol == arcade.key.UP:
            self.p1_sprite.thrust = 0
        elif symbol == arcade.key.DOWN:
            self.p1_sprite.thrust = 0
        elif symbol == arcade.key.A:
            self.p2_sprite.change_angle = 0
        elif symbol == arcade.key.D:
            self.p2_sprite.change_angle = 0
        elif symbol == arcade.key.W:
            self.p2_sprite.thrust = 0
        elif symbol == arcade.key.S:
            self.p2_sprite.thrust = 0

    def on_update(self, x):

        self.frame_count += 1

        if not self.game_over:
            self.all_sprites_list.update()
            
            for bullet in self.bullet_list:
                wall_plain = arcade.check_for_collision_with_list(bullet, self.wall_list)
                wall_spatial = arcade.check_for_collision_with_list(bullet, self.wall_list)
                if len(wall_plain) != len(wall_spatial):
                    print("ERROR")

                wall = wall_spatial

                for wall in walls:
                    bullet.remove_from_sprite_lists()
        
        if not self.p1_sprite.respawning:
                bullets = arcade.check_for_collision_with_list(self.p1_sprite, self.bullet_list)

                if len(bullets) > 0:
                    if self.p1_lives > 0:
                        self.p1_lives -= 1
                        self.p1_sprite.respawn()
                        self.p1_life_list.pop().remove_from_sprite_lists()
                        print("Shot")
                    else:
                        self.game_over = True
                        print("Player 2 winner!")
        
        if not self.p2_sprite.respawning:
                bullets = arcade.check_for_collision_with_list(self.p2_sprite, self.bullet_list)

                if len(bullets) > 0:
                    if self.p2_lives > 0:
                        self.p2_lives -= 1
                        self.p2_sprite.respawn()
                        self.p2_life_list.pop().remove_from_sprite_lists()
                        print("Shot")
                    else:
                        self.game_over = True
                        print("Player 1 winner!")

