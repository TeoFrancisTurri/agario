import threading
from server.match.match import Match


class MatchManager:
    def __init__(self):
        self.lock = threading.Lock()
        self.match = Match(match_id=1)
        self.match.start()

    def add_client(self, client_handler, username):
        with self.lock:
            self.match.add_client(client_handler, username)
            client_handler.match = self.match

    def remove_client(self, client_handler):
        with self.lock:
            if client_handler.match is not None:
                client_handler.match.remove_client(client_handler)
                client_handler.match = None

    def stop(self):
        with self.lock:
            self.match.stop()