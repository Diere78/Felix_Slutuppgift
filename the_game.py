import random
import math
import arcade
import os
import settings
from typing import cast
from object_classes import TurningSprite, BulletSprite, WallSprite, CharacterSprite


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

        self.bullets = BulletSprite("sprites/bullet.png", settings.BULLET_SCALE)

        self.p1_sprite = None
        self.p1_lives = settings.LIVES - 1
        self.p2_sprite = None
        self.p2_lives = settings.LIVES - 1


    def startGame(self):

        self.frame_count = 0
        self.game_over = False
        self.victory_text = ""

        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.p1_sprite = CharacterSprite("sprites/tank_green.png", settings.SPRITE_SCALE)
        self.p1_sprite.center_x = 650
        self.p1_sprite.center_y = 650
        self.p1_sprite.angle = 180 
        self.all_sprites_list.append(self.p1_sprite)
        self.p1_lives = settings.LIVES - 1

        self.p2_sprite = CharacterSprite("sprites/tank_blue.png", settings.SPRITE_SCALE)
        self.p2_sprite.center_x = 650
        self.p2_sprite.center_y = 100
        self.all_sprites_list.append(self.p2_sprite)
        self.p2_lives = settings.LIVES - 1

        parallel_rows = [150, 550]
        parallel_lines = [150, 350, 550, 750, 950, 1150]
        vertical_lines = [375, 650, 925]
        
        for line in parallel_lines:
            for row in parallel_rows:
                wall_sprite = WallSprite("sprites/red_wall.png", settings.WALL_SCALE)
                wall_sprite.center_x = line
                wall_sprite.center_y = row
                self.all_sprites_list.append(wall_sprite)
                self.wall_list.append(wall_sprite)

        for wall in vertical_lines:
            wall_sprite = WallSprite("sprites/blue_wall.png", settings.BLUE_SCALE)
            wall_sprite.center_x = wall
            wall_sprite.center_y = 350
            self.all_sprites_list.append(wall_sprite)
            self.wall_list.append(wall_sprite)

    def on_draw(self):

        arcade.start_render() 

        if not self.game_over:
            self.all_sprites_list.draw()

            output = f"Player 1 Lives:  {(self.p1_lives + 1)}"
            arcade.draw_text(output, 10, 50, arcade.color.WHITE, 13) 

            output = f"Player 2 Lives:  {(self.p2_lives + 1)}"
            arcade.draw_text(output, 10, 10, arcade.color.WHITE, 13)

        else:
            output = f"{(self.victory_text)}"
            arcade.draw_text(output, 425, 500, arcade.color.WHITE, 60)

            output = f"Press 'R' to Restart"
            arcade.draw_text(output, 500, 200, arcade.color.WHITE, 30)



            

    def on_key_press(self, symbol, modifiers):

        if not self.p1_sprite.respawning and symbol == arcade.key.SPACE:
            bullet_sprite = self.bullets
            bullet_sprite.guid = "Bullet"

            bullet_speed = 40
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
            bullet_sprite = bullet_sprite = self.bullets
            bullet_sprite.guid = "Bullet"

            bullet_speed = 40
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
            self.p1_sprite.angle = 90
            self.p1_sprite.speed = settings.PACE
        elif symbol == arcade.key.RIGHT:
            self.p1_sprite.angle = 270
            self.p1_sprite.speed = settings.PACE
        elif symbol == arcade.key.UP:
            self.p1_sprite.angle = 0
            self.p1_sprite.speed = settings.PACE
        elif symbol == arcade.key.DOWN:
            self.p1_sprite.angle = 180
            self.p1_sprite.speed = settings.PACE
        elif symbol == arcade.key.ESCAPE:
            exit()
        elif symbol == arcade.key.A:
            self.p2_sprite.angle = 90
            self.p2_sprite.speed = settings.PACE
        elif symbol == arcade.key.D:
            self.p2_sprite.angle = 270
            self.p2_sprite.speed = settings.PACE
        elif symbol == arcade.key.W:
            self.p2_sprite.angle = 0
            self.p2_sprite.speed = settings.PACE
        elif symbol == arcade.key.S:
            self.p2_sprite.angle = 180
            self.p2_sprite.speed = settings.PACE
        elif symbol == arcade.key.R:
            self.startGame()

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            if self.p1_sprite.angle == 90:
                self.p1_sprite.speed = 0  
        elif symbol == arcade.key.RIGHT:
            if self.p1_sprite.angle == 270:
                self.p1_sprite.speed = 0
        elif symbol == arcade.key.UP:
            if self.p1_sprite.angle == 0:
                self.p1_sprite.speed = 0
        elif symbol == arcade.key.DOWN:
            if self.p1_sprite.angle == 180:
                self.p1_sprite.speed = 0
        elif symbol == arcade.key.A:
            if self.p2_sprite.angle == 90:
                self.p2_sprite.speed = 0
        elif symbol == arcade.key.D:
            if self.p2_sprite.angle == 270:
                self.p2_sprite.speed = 0
        elif symbol == arcade.key.W:
            if self.p2_sprite.angle == 0:
                self.p2_sprite.speed = 0
        elif symbol == arcade.key.S:
            if self.p2_sprite.angle == 180:
                self.p2_sprite.speed = 0

    def on_update(self, x):

        self.frame_count += 1

        if not self.game_over:
            p1_pos_x = self.p1_sprite.center_x
            p1_pos_y = self.p1_sprite.center_y

            p2_pos_x = self.p2_sprite.center_x
            p2_pos_y = self.p2_sprite.center_y
            self.all_sprites_list.update()
            
            walls_block_p1 = arcade.check_for_collision_with_list(self.p1_sprite, self.wall_list)
            walls_block_p2 = arcade.check_for_collision_with_list(self.p2_sprite, self.wall_list)

            if len(walls_block_p1) > 0:
                self.p1_sprite.center_x = p1_pos_x
                self.p1_sprite.center_y = p1_pos_y


            if len(walls_block_p2) > 0:
                self.p2_sprite.center_x = p2_pos_x
                self.p2_sprite.center_y = p2_pos_y

            if p1_pos_x == settings.LEFT_LIMIT:
                self.p1_sprite.center_x = p1_pos_x + 6
            elif p1_pos_x == settings.RIGHT_LIMIT:
                self.p1_sprite.center_x = p1_pos_x - 6
            elif p1_pos_y == settings.TOP_LIMIT:
                self.p1_sprite.center_y = p1_pos_y - 6
            elif p1_pos_y == settings.BOTTOM_LIMIT:
                self.p1_sprite.center_y = p1_pos_y + 6
            if p2_pos_x == settings.LEFT_LIMIT:
                self.p2_sprite.center_x = p2_pos_x + 6
            elif p2_pos_x == settings.RIGHT_LIMIT:
                self.p2_sprite.center_x = p2_pos_x - 6
            elif p2_pos_y == settings.TOP_LIMIT:
                self.p2_sprite.center_y = p2_pos_y - 6
            elif p2_pos_y == settings.BOTTOM_LIMIT:
                self.p2_sprite.center_y = p2_pos_y + 6

            for bullet in self.bullet_list:
                walls_plain = arcade.check_for_collision_with_list(bullet, self.wall_list)
                walls_spatial = arcade.check_for_collision_with_list(bullet, self.wall_list)


                if len(walls_plain) != len(walls_spatial):
                    print("ERROR")
                if len(walls_plain) > 0 or len(walls_spatial) > 0:
                    bullet.remove_from_sprite_lists()
            
        if not self.p1_sprite.respawning:
                bullets = arcade.check_for_collision_with_list(self.p1_sprite, self.bullet_list)

                if len(bullets) > 0:
                    if self.p1_lives > 0:
                        self.p1_lives -= 1
                        self.p1_sprite.respawn()
                        self.p1_sprite.center_x = 650
                        self.p1_sprite.center_y = 650
                        self.p1_sprite.angle = 180
                        print("Shot")
                    else:
                        self.victory_text = "Player 2 wins!"
                        self.game_over = True
        
        if not self.p2_sprite.respawning:
                bullets = arcade.check_for_collision_with_list(self.p2_sprite, self.bullet_list)

                if len(bullets) > 0:
                    if self.p2_lives > 0:
                        self.p2_lives -= 1
                        self.p2_sprite.respawn()
                        self.p2_sprite.center_x = 650
                        self.p2_sprite.center_y = 100
                        self.p2_sprite.angle = 0
                        print("Shot")
                    else:
                        self.victory_text = "Player 1 wins!"
                        self.game_over = True

