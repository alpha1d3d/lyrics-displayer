import requests

import html2text

from .main import LyricSource


class GeniusSource(LyricSource):
    ROOT = 'https://genius.com/'

    def __init__(self):
        h = html2text.HTML2Text()
        h.ignore_links = True
        self.html_handler = h

    def get_lyrics(self, artist, title):
        url = '{}api/search/lyric?page=1&q={}+{}'.format(
            self.ROOT, artist,
            title.split('(')[0]
        ).replace(' ', '+')

        print('Querying: {}'.format(url))
        try:
            response = requests.get(url)
            song_id = (
                response.json()
                ['response']
                ['sections'][0]
                ['hits'][0]
                ['result']['id']
            )
        except Exception:
            return

        url = '{}/songs/{}/embed.js'.format(self.ROOT, song_id)
        response = requests.get(url)
        lyrics = (
            response.text
            .split('<div class=\\\\\\"rg_embed_body\\\\\\">', 1)[1]
            .split('<div class=\\\\\\"rg_embed_footer\\\\\\">')[0]
        ).replace('\\n', '').replace('\\', '')

        lyrics = self.html_handler.handle(lyrics).split('\n')

        return lyrics
