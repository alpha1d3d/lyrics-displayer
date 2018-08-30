from __future__ import absolute_import

import time
import sys
import os
import select

from lyricfetch import get_lyrics, Song

from .players.sonos import SonosPlayer
from .utils import duration_string_to_seconds, display_lyrics


def run():
    player = SonosPlayer()

    if not player.connected:
        return

    stop = False
    not_playing = False
    while True:
        track = player.get_track_info()
        time.sleep(1)

        if not track['title']:
            if not not_playing:
                print('Nothing playing')
                not_playing = True
            continue

        # estimate position
        duration = duration_string_to_seconds(track['duration'])
        position = duration_string_to_seconds(track['position'])

        # instantiate song
        song = Song.from_info(track['artist'], track['title'])
        # fetch lyrics
        get_lyrics(song)
        # read lyrics
        lyrics = song.lyrics.split('\n')

        while True:
            os.system('clear')

            # calculate location
            percent = position / duration
            location = int(round(percent * len(lyrics), 0))

            # if ended exit
            if location >= len(lyrics):
                break

            # display lyrics
            display_lyrics(lyrics, track, location, position)

            # refresh display in a second
            time.sleep(1)
            position += 1

            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                input()
                stop = True
                break

        if stop:
            break
