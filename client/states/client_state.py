class ClientState:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass