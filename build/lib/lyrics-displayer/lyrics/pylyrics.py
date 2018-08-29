from PyLyrics.functions import PyLyrics

from .main import LyricSource


class PyLyricsSource(LyricSource):
    def get_lyrics(self, artist, title):
        try:
            lyrics = PyLyrics.getLyrics(artist, title).split('\n')
        except Exception:
            return
        return lyrics
