from collections import OrderedDict

import soco

from .main import Player


class SonosPlayer(Player):
    def connect_player(self):
        players = list(soco.discover())
        players = OrderedDict({sonos.player_name: sonos for sonos in players})

        print('Available Sonos Players:')
        print('\n'.join(
            '{}) {}'.format(i + 1, sonos)
            for i, sonos in enumerate(players.keys())
        ))

        prompt = (
            'Please select the Sonos Player' +
            ' to connect to (or the first player in the group):\n'
        )
        tries = 0
        while tries < 3:
            sonos_id = input(prompt)

            if not sonos_id:
                return

            try:
                sonos_id = int(sonos_id)
            except ValueError:
                if sonos_id not in players.keys():
                    print('Invalid choice\n')
                    tries += 1
                    continue
            else:
                if int(sonos_id) not in range(1, len(players) + 1):
                    print('Invalid choice\n')
                    tries += 1
                    continue
            break
        else:
            return

        try:
            sonos_id = int(sonos_id)
        except ValueError:
            found_ip = players[sonos_id].ip_address
        else:
            found_ip = list(players.items())[int(sonos_id) - 1][1].ip_address

        print('Located sonos system //{}'.format(found_ip))
        return soco.SoCo(found_ip)

    def get_track_info(self):
        return self.player.get_current_track_info()
