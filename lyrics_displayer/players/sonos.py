from collections import OrderedDict

import soco

from .main import Player


class SonosPlayer(Player):
    def connect_player(self):
        # discover available sonos players
        self.players = OrderedDict({
            sonos.player_name: sonos
            for sonos in soco.discover()
        })

        print('Available Sonos Players:')
        print('\n'.join(
            '{}) {}'.format(i + 1, sonos)
            for i, sonos in enumerate(self.players.keys())
        ))

        # get the user choice
        sonos_id = self._user_input_choice()
        if not sonos_id:
            return

        # retrieve the IP address
        found_ip = self._retrieve_ip(sonos_id)
        print('Located sonos system //{}'.format(found_ip))

        return soco.SoCo(found_ip)

    def _user_input_choice(self):
        prompt = (
            'Please select the Sonos Player' +
            ' to connect to (or the first player in the group):\n'
        )
        # valid choices are either player names
        valid_choices = set(self.players.keys())
        # or the index in the printed list
        valid_choices |= set(range(1, len(self.players) + 1))

        tries = 0
        while tries < 3:
            sonos_id = input(prompt)

            if not sonos_id:
                return

            try:
                sonos_id = int(sonos_id)
            except ValueError:
                pass

            if sonos_id not in valid_choices:
                print('Invalid choice\n')
                tries += 1
                continue

            return sonos_id

    def _retrieve_ip(self, sonos_id):
        try:
            sonos_id = int(sonos_id)
        except ValueError:
            # sonos_id is either a string (player name)
            sonos = self.players[sonos_id]
        else:
            # or an integer (index in printed list)
            sonos = list(self.players.items())[int(sonos_id) - 1][1]
        return sonos.ip_address

    def get_track_info(self):
        return self.player.get_current_track_info()
