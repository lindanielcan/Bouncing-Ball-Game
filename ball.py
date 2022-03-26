import pygame
from random import choice


class Ball:
    def __init__(self, x_cor, y_cor, screen, setting):
        """A bouncing ball"""
        self.setting = setting
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.screen = screen
        self.image = ""
        self.ball_color = (255, 0, 0)
        self.ball_height = 30
        self.ball_width = 30
        self.ball = pygame.transform.scale(pygame.image.
                                           load('images/tennis.png'), [self.ball_width, self.ball_height]).convert_alpha(screen)
        self.ball_rect = ''
        # 1 through 4 stands for quadrants 1 through 4.
        self.ball_direction = [1, 2, 3, 4]
        # randomize the direction of the ball
        self.dir = choice(self.ball_direction)

        self.change_ball_dir_once = 1

        self.moving_distance = 1

    def set_ball_position(self):
        """Set the ball position."""

        self.ball_rect = self.ball.get_rect(center=(self.x_cor, self.y_cor))
        self.screen.blit(self.ball, self.ball_rect)

    def move_ball(self):
        """move ball"""

        if self.dir == 1:
            self.move_ball_right()
            self.move_ball_up()
        elif self.dir == 2:
            self.move_ball_left()
            self.move_ball_up()
        elif self.dir == 3:
            self.move_ball_down()
            self.move_ball_left()
        elif self.dir == 4:
            self.move_ball_right()
            self.move_ball_down()

        self.ball_hit_wall()

    def ball_hit_wall(self):
        """change ball direction when it hits a wall"""
        if self.x_cor <= 15:
            if self.dir == 2:
                self.dir = 1
            elif self.dir == 3:
                self.dir = 4
        elif self.x_cor >= self.setting.screen_width - (self.ball_width / 2):
            if self.dir == 1:
                self.dir = 2
            elif self.dir == 4:
                self.dir = 3
        elif self.y_cor <= 15:
            if self.dir == 1:
                self.dir = 4
            elif self.dir == 2:
                self.dir = 3
        elif self.y_cor >= self.setting.screen_height - (self.ball_height / 2):
            if self.dir == 4:
                self.dir = 1
            elif self.dir == 3:
                self.dir = 2

    def ball_hit_object(self):
        """Check direction of the ball when it hits an object."""
        if self.dir == 1:
            self.dir = 4
        elif self.dir == 2:
            self.dir = 3
        elif self.dir == 3:
            self.dir = 2
        elif self.dir == 4:
            self.dir = 1

    def move_ball_right(self):
        self.x_cor += self.moving_distance

    def move_ball_left(self):
        self.x_cor -= self.moving_distance

    def move_ball_up(self):
        self.y_cor -= self.moving_distance

    def move_ball_down(self):
        self.y_cor += self.moving_distance

    def ball_did_collide(self, rect):
        """Checks if the ball collide with any object."""

        collide = self.ball_rect.colliderect(rect)
        if collide:
            self.ball_hit_object()
            return True
