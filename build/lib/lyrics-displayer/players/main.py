

class Player(object):
    def __init__(self):
        self.player = self.connect_player()
        self.connected = bool(self.player)

    def connect_player(self):
        raise NotImplementedError
        return 'player'

    def get_track_info(self):
        raise NotImplementedError
        return {
            'artist': '',
            'title': '',
            'duration': '',
            'position': '',
        }
