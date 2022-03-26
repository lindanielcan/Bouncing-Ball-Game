import pygame, sys
from setting import Setting
from ball import Ball
from random import randint
from obstacle import Obstacle


class Game:
    def __init__(self):
        pygame.init()

        # Screen setting.
        self.setting = Setting()
        self.screen = pygame.display. \
            set_mode(self.setting.screen_size)
        # Ball setting
        self.ball = Ball(randint(0, self.setting.screen_size[0]),
                         randint(0, self.setting.screen_size[1]), self.screen, self.setting)

        self.mouse_only_left_clicked_once = True
        self.mouse_only_right_clicked_once = True
        self.mouse_position = []

        self.clock = pygame.time.Clock()
        self.index = 0

        self.obstacle = Obstacle(self.screen)
        self.obstacle_list = []
        self.obstacle_position_list = []

    def run_game(self):
        """This function is responsible to
        get the game to start running."""

        # FramePerSec = pygame.time.Clock()

        while True:
            self.index += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Fill in screen background color.
            self.screen.fill(self.setting.
                             back_ground_color)

            # by checking on mouse_only_clicked_once == 1,
            # we can assure that when the mouse is pressed, it only perform the task once.
            # if we don't define mouse_only_clicked_once == 1,
            # tasks might be performed multiple times when mouse is pressed.
            if self.mouse_only_left_clicked_once == 1 and self.mouse_left_clicked() == True:
                self.mouse_position = [int(pygame.mouse.get_pos()[0]), int(pygame.mouse.get_pos()[1])]

                # # check when the user draws a new obstacle, it's not colliding with any existing ones.
                # if self.did_obstacle_collide_with_one_another((self.mouse_position[0], self.mouse_position[1])):
                self.obstacle_position_list.append(self.mouse_position)

                self.obstacle_list.append(self.obstacle)
                self.mouse_only_left_clicked_once = 0

                print(len(self.obstacle_list), ' ', len(self.obstacle_position_list))

                self.obstacle_list.append(self.obstacle)
                self.mouse_only_left_clicked_once = 0

                # if len(self.obstacle_list) >= 1:
                #     for item in self.obstacle_list:
                #         if not item.did_obstacle_collide_with_one_another((self.mouse_position[0],
                #                                                            self.mouse_position[1])):
                #
                #
            elif self.mouse_only_right_clicked_once == 1 and self.mouse_right_clicked() == True:
                self.mouse_only_right_clicked_once = 0

            # Reset it to 1 every time when index variable is divisible by 150.
            if self.index % 50 == 0:
                self.mouse_only_left_clicked_once = True
                self.mouse_only_right_clicked_once = True

            # draw obstacle from the obstacle position list.
            if self.obstacle_position_list:

                for index in range(0, len(self.obstacle_position_list)):
                    self.obstacle_list[index].draw_obstacle(self.obstacle_position_list[index][0],
                                                            self.obstacle_position_list[index][1])

                    # Check if the ball is colliding with any object.
                    if self.ball.ball_did_collide(self.obstacle_list[index].obs_rect):
                        break

            # FramePerSec.tick(self.setting.time_delays)

            self.ball.set_ball_position()
            self.ball.move_ball()

            # self.clock.tick(self.setting.time_delays)
            pygame.display.update()

    def mouse_left_clicked(self):
        """
        Detecting if the user pressed the left button on the mouse.
        :return: boolean - if mouse is left pressed.
        """
        return pygame.mouse.get_pressed()[0]

    def mouse_right_clicked(self):
        """
        Detecting if the user pressed the right button on the mouse.
        :return: boolean - if mouse is right pressed.
        """
        return pygame.mouse.get_pressed()[2]
