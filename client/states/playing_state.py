from client.states.client_state import ClientState


class PlayingState(ClientState):
    def draw(self):
        self.screen.fill((230, 230, 230))