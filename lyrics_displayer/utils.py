''' List of generic utils functions
'''


def duration_string_to_seconds(string):
    ''' Converts a string representation of duration
        into total seconds in float.

        >>>  duration_string_to_seconds('00:03:16')
        196
    '''
    duration = string.split(':')
    return (
        int(duration[0]) * 60 * 60 +
        int(duration[1]) * 60 +
        int(duration[2])
    )


def duration_seconds_to_string(seconds):
    ''' Converts a total amount of seconds into a
        string representation of duration.

        >>>  duration_seconds_to_string(196)
        '00:03:16'
    '''
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f'{h}:{m:02}:{s:02}'


def display_lyrics(lyrics, track, location, position):
    '''
        Deals with formatting the lyrics unto the screen.

        Displays the lyrics on a 30 rows moving window.
    '''
    display_rows = 15

    separator = '-' * 60
    end = len(lyrics)

    combine_lyrics = '\n'.join([
        ('@ ' if i == location else '| ') + row
        for i, row in
        enumerate(lyrics[
            max([0, min([end - (display_rows * 2), location - display_rows])]):
            max([display_rows * 2, location + display_rows])
        ])
    ])
    current_timer = duration_seconds_to_string(position)
    print(
        '\n'.join([
              f'{separator}',
              f' {track["artist"]} - {track["title"]}',
              f'{separator}',
              '...' if location > display_rows else '',
              f'{combine_lyrics}',
              '...' if location < end - display_rows else '',
              f'{separator}',
              f' {current_timer} / {track["duration"]}',
              f'{separator}',
              'Press ENTER to exit',
        ])
    )
