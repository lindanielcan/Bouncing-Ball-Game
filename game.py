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

        # Initialize these variables to make sure operations are only perform once when mouse is clicked.
        self.mouse_only_left_clicked_once = True
        self.mouse_only_right_clicked_once = True

        # When mouse is clicked, positions of the mouse should be recorded and stored.
        self.mouse_positions = []

        self.clock = pygame.time.Clock()
        self.index = 0

        self.obstacle_position_list = []
        self.obstacle_list = []

        # initializing mouse position in a tuple.
        self.mouse_position = ()
        self.right_mouse_click_position = ()
        self.collided_rect_index = 0

    def run_game(self):
        """This function is responsible to
        get the game to start running."""

        # FramePerSec = pygame.time.Clock()

        while True:

            self.index += 1

            # Fill in screen background color.
            self.screen.fill(self.setting.
                             back_ground_color)

            # check for event from the keyboard and the mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # listen mouse events.
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Things should happen when left clicked.
                    if event.button == 1:
                        self.mouse_position = pygame.mouse.get_pos()
                        # No particular condition should be met before draw the first obstacle.
                        if len(self.obstacle_position_list) == 0:
                            self.record_and_appending_obstacle()
                        else:
                            # Need to check is one obstacle is colliding with another before appending it.
                            if self.did_collide_with_any_rect(self.mouse_position):
                                # if one collides with one another in the list, pop the last one in the list.
                                self.record_and_appending_obstacle()
                                self.obstacle_position_list.pop(len(self.obstacle_position_list) - 1)
                                self.obstacle_list.pop(len(self.obstacle_list) - 1)
                            # # if one does not collide with others, then it's safe to append it.
                            else:
                                self.record_and_appending_obstacle()
                    # Things should happen when right clicked.
                    elif event.button == 3:
                        self.right_mouse_click_position = pygame.mouse.get_pos()

                        # This event should do nothing if the length of the obstacle list is empty
                        if len(self.obstacle_list) != 0:
                            # check if the point collides with any of the rect in the list.
                            if self.did_collide_with_any_rect(self.right_mouse_click_position):
                                self.obstacle_list.pop(self.collided_rect_index)
                                self.obstacle_position_list.pop(self.collided_rect_index)

            # Obstacle.
            # Draw obstacles.
            if len(self.obstacle_position_list) != 0:
                for index in range(0, len(self.obstacle_position_list)):
                    self.obstacle_list[index].draw_obstacle(self.obstacle_position_list[index][0],
                                                            self.obstacle_position_list[index][1])

            # Ball.
            self.ball.draw_ball()
            self.ball.move_ball()

            if len(self.obstacle_list) != 0:
                self.ball.ball_did_collide(self.obstacle_list)

            pygame.display.update()

            # self.clock.tick(self.setting.time_delays)

    def did_collide_with_any_rect(self, point):
        """Checks if a point collides with any rect."""
        obstacle_collision = []
        for rect in self.obstacle_list:
            if rect.is_point_in_a_rect(point):
                self.collided_rect_index = self.obstacle_list.index(rect)
                obstacle_collision.append(True)
            else:
                obstacle_collision.append(False)
        # If all the variable in the list are not True, then it means the last obstacle appended did not collide
        # with previous appended obstacles.
        if not any(obstacle_collision):
            return False
        else:
            return True

    def record_and_appending_obstacle(self):
        """Append new obstacle and its position into lists."""
        # Store the mouse position in a list, mouse.get_pos() returns a tuple.
        self.obstacle_position_list.append(self.mouse_position)
        # Create an obstacle and it should be stored in a list
        self.obstacle_list.append(Obstacle(self.screen))
