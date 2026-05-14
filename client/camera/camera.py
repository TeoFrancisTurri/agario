class Camera:
    def __init__(self, screen_width, screen_height):
        self.x = 0
        self.y = 0

        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, target_x, target_y):
        self.x = target_x - self.screen_width // 2
        self.y = target_y - self.screen_height // 2

    def apply(self, x, y):
        return (
            x - self.x,
            y - self.y
        )