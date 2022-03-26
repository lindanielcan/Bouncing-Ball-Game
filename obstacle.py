import pygame


class Obstacle:
    def __init__(self, screen):
        self.obs_width = 50
        self.obs_height = 50
        self.image = 'images/rock.png'
        self.obs = pygame.transform.scale(pygame.image.
                                          load(self.image), [self.obs_width, self.obs_height]).convert_alpha()
        self.obs_rect = ''
        self.screen = screen

    def draw_obstacle(self, x_cor, y_cor):
        """Draws a obstacle on the screen."""
        self.obs_rect = self.obs.get_rect(center=(x_cor, y_cor))
        self.screen.blit(self.obs, self.obs_rect)

    def did_obstacle_collide_with_one_another(self, point):

        collide = self.obs_rect.collidepoint(point)
        if collide:
            return True
        else:
            return False
