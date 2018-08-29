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
    return '{}:{:02}:{:02}'.format(h, m, s)


def display_lyrics(lyrics, track, location, position):
    separator = '-' * 60
    combine_lyrics = [
        ('~ ' if i == location else '| ') +
        row for i, row in enumerate(lyrics)
    ]
    print(
        '\n'.join([
              ' {artist}',
              '{separator}',
              ' {title}',
              '{separator}',
        ] + combine_lyrics + [
              '{separator}',
              ' {current_timer} / {duration}',
              '{separator}',
              'Press ENTER to exit',
        ]).format(
              separator=separator,
              current_timer=duration_seconds_to_string(position),
              **track
        )
    )
