import pygame

from client.config.client_settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WINDOW_TITLE
from client.config.colors import BACKGROUND_COLOR, GRID_COLOR
from client.states.main_menu_state import MainMenuState


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True
        pygame.key.set_repeat(400, 40)
        
        self.state = MainMenuState(self)
        self.state.enter()

    def change_state(self, new_state):
        self.state.exit()
        self.state = new_state
        self.state.enter()

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.state.handle_event(event)

            self.state.update(dt)
            self.state.draw()

            pygame.display.flip()

        pygame.quit()

    def draw_grid(self):
        grid_size = 50

        width = self.screen.get_width()
        height = self.screen.get_height()

        for x in range(0, width, grid_size):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, height))

        for y in range(0, height, grid_size):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (width, y))