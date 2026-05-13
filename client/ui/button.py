import pygame


class Button:
    def __init__(
        self,
        rect,
        text,
        background_color=(70, 70, 70),
        text_color=(255, 255, 255),
        hover_color=(90, 90, 90),
    ):
        self.rect = pygame.Rect(rect)

        self.text = text

        self.background_color = background_color
        self.text_color = text_color
        self.hover_color = hover_color

        self.font = pygame.font.SysFont(None, 36)

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        color = self.background_color

        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=8
        )

        text_surface = self.font.render(
            self.text,
            True,
            self.text_color
        )

        text_rect = text_surface.get_rect(
            center=self.rect.center
        )

        screen.blit(text_surface, text_rect)