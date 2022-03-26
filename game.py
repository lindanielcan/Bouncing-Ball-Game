import pygame, sys
from setting import Setting
from ball import Ball
from random import randint

class Game:
    def __init__(self):
        pygame.init()

        # Screen setting.
        self.setting = Setting()
        self.screen = pygame.display.\
            set_mode(self.setting.screen_size)
        # Ball setting
        self.ball = Ball(randint(0, self.setting.screen_size[0]),
                         randint(0, self.setting.screen_size[1]), self.screen)


    def run_game(self):
        """This function is responsible to
        get the game to start running."""

        FramePerSec = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.setting.
                             back_ground_color)

            self.ball.set_ball_position()

            pygame.display.flip()
