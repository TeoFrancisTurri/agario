import pygame


class TextInput:
    def __init__(
        self,
        rect,
        placeholder="Username",
        max_length=16,
    ):
        self.rect = pygame.Rect(rect)

        self.text = ""
        self.placeholder = placeholder

        self.max_length = max_length

        self.active = False

        self.font = pygame.font.SysFont(None, 36)

        self.background_color = (255, 255, 255)

        self.border_color = (140, 140, 140)
        self.active_border_color = (80, 160, 255)

        self.text_color = (30, 30, 30)
        self.placeholder_color = (150, 150, 150)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]

            elif len(self.text) < self.max_length:
                if event.unicode.isprintable():
                    self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.background_color,
            self.rect,
            border_radius=8
        )

        border_color = self.border_color

        if self.active:
            border_color = self.active_border_color

        pygame.draw.rect(
            screen,
            border_color,
            self.rect,
            2,
            border_radius=8
        )

        if self.text == "":
            text_surface = self.font.render(
                self.placeholder,
                True,
                self.placeholder_color
            )
        else:
            text_surface = self.font.render(
                self.text,
                True,
                self.text_color
            )

        text_rect = text_surface.get_rect(
            midleft=(self.rect.x + 12, self.rect.centery)
        )

        screen.blit(text_surface, text_rect)