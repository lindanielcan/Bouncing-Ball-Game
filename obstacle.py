import pygame


class Obstacle:
    def __init__(self, screen):

        """The class draws an obstacle with specific position on the screen."""

        self.screen = screen

        # Resize the image.
        self.image = 'images/rock.png'
        self.obs_width = 50
        self.obs_height = 50
        self.obs = pygame.transform.scale(pygame.image.
                                          load(self.image), [self.obs_width, self.obs_height]).convert_alpha()
        # create a rect surface.
        self.obs_rect = self.obs.get_rect(center=(-50, -50))

    def draw_obstacle(self, x_cor, y_cor):
        """Draws a obstacle on the screen."""
        self.obs_rect = self.obs.get_rect(center=(x_cor, y_cor))
        self.screen.blit(self.obs, self.obs_rect)

    def is_point_in_a_rect(self, point):
        """Checks if one point collide with a rect."""
        collide = self.obs_rect.collidepoint(point[0], point[1])

        if collide:
            return True
        else:
            return False
