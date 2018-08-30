from __future__ import absolute_import

import time
import sys
import os
import select

from lyricfetch import get_lyrics, Song

from .players.sonos import SonosPlayer
from .utils import (
    duration_seconds_to_string,
    duration_string_to_seconds,
)


def retrieve_lyrics(track):
    # instantiate song
    song = Song.from_info(track['artist'], track['title'])
    # fetch lyrics
    get_lyrics(song)
    # read lyrics
    lyrics = song.lyrics.split('\n')
    return lyrics


def get_track_info(player):
    track = player.get_track_info()

    track['location'] = 0
    track['duration_secs'] = duration_string_to_seconds(track['duration'])
    track['position_secs'] = duration_string_to_seconds(track['position'])
    return track


def update_track_info(track):
    # calculate location
    percent = track['position_secs'] / track['duration_secs']
    track['location'] = int(round(percent * track['length'], 0))
    track['position'] = duration_seconds_to_string(track['position_secs'])
    return track


def display_lyrics(lyrics, track):
    '''
        Deals with formatting the lyrics unto the screen.

        Displays the lyrics on a 30 rows moving window.
    '''
    display_rows = 15
    separator = '-' * 60

    combine_lyrics = '\n'.join([
        ('@ ' if i == track['location'] else '| ') + row
        for i, row in
        enumerate(lyrics[
            max([0, min([
                track['length'] - (display_rows * 2),
                track['location'] - display_rows]
            )]):
            max([display_rows * 2, track['location'] + display_rows])
        ])
    ])
    print(
        '\n'.join([
              f'{separator}',
              f' {track["artist"]} - {track["title"]}',
              f'{separator}',
              '...' if track['location'] > display_rows else '',
              f'{combine_lyrics}',
              '...' if track['location'] < track['length'] - display_rows
              else '',
              f'{separator}',
              f' {track["position"]} / {track["duration"]}',
              f'{separator}',
              'Press ENTER to exit',
        ])
    )


def run():
    player = SonosPlayer()
    if not player.connected:
        return

    stop = False
    not_playing = False
    while True:
        track = get_track_info(player)

        if not track['title']:
            if not not_playing:
                print('Nothing playing')
                not_playing = True
            continue

        lyrics = retrieve_lyrics(track)
        track['length'] = len(lyrics)

        while True:
            os.system('clear')

            # display lyrics
            display_lyrics(lyrics, track)

            # refresh display in a second
            time.sleep(1)
            track['position_secs'] += 1
            track = update_track_info(track)

            # if ended exit
            if track['position_secs'] >= track['duration_secs']:
                break

            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                input()
                stop = True
                break

        if stop:
            break
